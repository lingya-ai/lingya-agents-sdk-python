"""Trusted-server HMAC client for the Lingya Agents OpenAPI."""

from __future__ import annotations

import base64
import hashlib
import hmac
import secrets
import time
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from typing import TypeVar
from urllib.parse import quote, urlencode

import httpx
from pydantic import BaseModel

from lingya_agents_sdk.events import AiChatBriefEvent, decode_ai_chat_brief_event
from lingya_agents_sdk.sse import decode_sse_lines

ModelT = TypeVar("ModelT", bound=BaseModel)


@dataclass(frozen=True)
class OpenApiCredentials:
    """服务端 OpenAPI 凭证；secret 不参与对象展示。 / Server credentials with a redacted secret."""

    access_key: str
    secret_key: str

    def __repr__(self) -> str:
        return f"OpenApiCredentials(access_key={self.access_key!r}, secret_key='<redacted>')"


@dataclass(frozen=True)
class QueryParameter:
    """保留顺序并允许重复名称的查询参数。 / Ordered query parameter that permits repeated names."""

    name: str
    value: str


class LingyaApiError(RuntimeError):
    """不包含凭证的 HTTP 错误。 / HTTP failure that never contains credentials."""

    def __init__(self, method: str, path: str, status_code: int, response_body: str) -> None:
        super().__init__(f"{method} {path} returned HTTP {status_code}")
        self.method = method
        self.path = path
        self.status_code = status_code
        self.response_body = response_body


class LingyaAgentsClient:
    """Lingya Agents SDK 入口，仅用于可信服务端。 / SDK entry point for trusted servers only."""

    def __init__(self, base_url: str, channel_id: str, credentials: OpenApiCredentials) -> None:
        if not channel_id:
            raise ValueError("channel_id must not be empty")
        self._base_url = base_url.rstrip("/")
        self.channel_id = channel_id
        self._credentials = credentials

    def for_user(self, external_user_id: str) -> LingyaAgentsUserClient:
        """绑定外部用户并为其后续请求独立签名。 / Bind one external user for subsequent signed calls."""
        return LingyaAgentsUserClient(self._base_url, self.channel_id, self._credentials, external_user_id)


class LingyaAgentsUserClient:
    """已绑定外部用户的同步客户端。 / Synchronous client bound to one external user."""

    def __init__(self, base_url: str, channel_id: str, credentials: OpenApiCredentials, external_user_id: str) -> None:
        user_bytes = external_user_id.encode("utf-8")
        if not 1 <= len(user_bytes) <= 256 or b"\0" in user_bytes:
            raise ValueError("external_user_id must contain 1 to 256 UTF-8 bytes and no NUL")
        self.channel_id = channel_id
        self._credentials = credentials
        self._encoded_user = base64.urlsafe_b64encode(user_bytes).rstrip(b"=").decode("ascii")
        self._root = f"{base_url}/api/agents/channel/openapi/v1/{quote(channel_id, safe='')}/chat"
        self._http = httpx.Client(timeout=httpx.Timeout(120.0), follow_redirects=False)

    def close(self) -> None:
        """释放连接池。 / Close the underlying connection pool."""
        self._http.close()

    def __enter__(self) -> LingyaAgentsUserClient:
        return self

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        self.close()

    def request_model(
        self,
        method: str,
        suffix: str,
        response_type: type[ModelT],
        body: BaseModel | str | None = None,
        query: Sequence[QueryParameter] = (),
    ) -> ModelT:
        """调用 JSON 接口并解析为明确 Pydantic 模型。 / Call a JSON endpoint and parse one explicit Pydantic model."""
        return response_type.model_validate_json(self.raw_response(method, suffix, body, query).content)

    def request_status(
        self,
        method: str,
        suffix: str,
        body: BaseModel | str | None = None,
        query: Sequence[QueryParameter] = (),
    ) -> int:
        """调用状态接口并返回 HTTP 状态码。 / Call a status endpoint and return its HTTP status."""
        return self.raw_response(method, suffix, body, query).status_code

    def request_bytes(self, method: str, suffix: str, query: Sequence[QueryParameter] = ()) -> bytes:
        """下载二进制响应。 / Download an exact binary response."""
        return self.raw_response(method, suffix, query=query, accept="application/octet-stream").content

    def raw_response(
        self,
        method: str,
        suffix: str,
        body: BaseModel | str | None = None,
        query: Sequence[QueryParameter] = (),
        accept: str = "application/json",
    ) -> httpx.Response:
        """发送受控底层请求；非成功状态转换为 [LingyaApiError]。 / Send a controlled request and reject non-success responses."""
        request = self._signed_request(method, suffix, body, query, accept)
        response = self._http.send(request)
        if not response.is_success:
            raise LingyaApiError(method, suffix, response.status_code, response.text)
        return response

    def stream_chat_events(self, conversation_id: str, message_id: str) -> Iterator[AiChatBriefEvent]:
        """订阅对话 SSE，并返回强类型事件或 raw JSON fallback。 / Stream typed conversation events with a raw-JSON fallback."""
        suffix = f"/conversations/{quote(conversation_id, safe='')}/stream"
        request = self._signed_request("POST", suffix, f'{{"messageId":"{message_id}"}}', (), "text/event-stream")
        response = self._http.send(request, stream=True)
        try:
            if not response.is_success:
                response.read()
                raise LingyaApiError("POST", suffix, response.status_code, response.text)
            for data in decode_sse_lines(response.iter_lines()):
                yield decode_ai_chat_brief_event(data)
        finally:
            response.close()

    def _signed_request(
        self,
        method: str,
        suffix: str,
        body: BaseModel | str | None,
        query: Sequence[QueryParameter],
        accept: str,
    ) -> httpx.Request:
        body_text = body.model_dump_json(by_alias=True, exclude_none=True) if isinstance(body, BaseModel) else body
        body_bytes = b"" if body_text is None else body_text.encode("utf-8")
        if len(body_bytes) > 2 * 1024 * 1024:
            raise ValueError("request body exceeds the 2 MiB signing limit")
        raw_query = urlencode([(item.name, item.value) for item in query])
        url = f"{self._root}{suffix}{'?' + raw_query if raw_query else ''}"
        timestamp = str(int(time.time()))
        nonce = base64.urlsafe_b64encode(secrets.token_bytes(16)).rstrip(b"=").decode("ascii")
        content_type = "application/json" if body_text is not None else ""
        canonical = "\n".join(
            [
                "OPENAPI-HMAC-SHA256-V1",
                self._credentials.access_key,
                timestamp,
                nonce,
                method.upper(),
                httpx.URL(url).raw_path.decode("ascii").split("?", 1)[0],
                raw_query,
                self._encoded_user,
                content_type,
                hashlib.sha256(body_bytes).hexdigest(),
            ]
        )
        signature = sign_canonical(self._credentials.secret_key, canonical)
        headers = {
            "Accept": accept,
            "X-OpenAPI-AK": self._credentials.access_key,
            "X-OpenAPI-Timestamp": timestamp,
            "X-OpenAPI-Nonce": nonce,
            "X-OpenAPI-User": self._encoded_user,
            "X-OpenAPI-Signature": signature,
        }
        if content_type:
            headers["Content-Type"] = content_type
        return self._http.build_request(method, url, headers=headers, content=body_bytes)


def sign_canonical(secret_key: str, canonical: str) -> str:
    """计算固定规范串的 HMAC，用于 golden vector 验证。 / Sign a deterministic canonical string for golden-vector tests."""
    return hmac.new(secret_key.encode("utf-8"), canonical.encode("utf-8"), hashlib.sha256).hexdigest()
