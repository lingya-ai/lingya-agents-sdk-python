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
from typing_extensions import deprecated

from lingya_agents_sdk.events import AiChatBriefEvent, decode_ai_chat_brief_event
from lingya_agents_sdk.models.ai_chat_stream_input import AiChatStreamInput
from lingya_agents_sdk.models.chat_stream_probe_event import ChatStreamProbeEvent
from lingya_agents_sdk.models.chat_stream_probe_input import ChatStreamProbeInput
from lingya_agents_sdk.sse import decode_sse_lines

ModelT = TypeVar("ModelT", bound=BaseModel)
RequestBody = BaseModel | Sequence[BaseModel] | str | None


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


class ApiError(RuntimeError):
    """不包含凭证的 HTTP 错误。 / HTTP failure that never contains credentials."""

    def __init__(self, method: str, path: str, status_code: int, response_body: str) -> None:
        super().__init__(f"{method} {path} returned HTTP {status_code}")
        self.method = method
        self.path = path
        self.status_code = status_code
        self.response_body = response_body


class AgentsClient:
    """Lingya Agents SDK 入口，仅用于可信服务端。 / SDK entry point for trusted servers only.

    客户端保存 channel 范围的凭证，但只有 [for_user()] 返回的用户客户端可以发起请求。
    """

    def __init__(self, base_url: str, channel_id: str, credentials: OpenApiCredentials) -> None:
        if not channel_id:
            raise ValueError("channel_id must not be empty")
        self._base_url = base_url.rstrip("/")
        self.channel_id = channel_id
        self._credentials = credentials

    def for_user(self, external_user_id: str) -> AgentsUserClient:
        """绑定外部用户并为其后续请求独立签名。 / Bind one external user for signed calls.

        Args:
            external_user_id: 调用方系统的稳定用户 ID，UTF-8 编码后为 1..256 字节且不能含 NUL。

        Returns:
            注入外部用户身份的同步客户端。
        """
        return AgentsUserClient(self._base_url, self.channel_id, self._credentials, external_user_id)


class AgentsUserClient:
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
        from lingya_agents_sdk.bound_api import (
            ChatApi,
            ConfigurationApi,
            ConversationsApi,
            EventsApi,
            FilesApi,
            InteractionsApi,
            KnowledgeApi,
            MessagesApi,
            SqlApi,
            WorkspaceApi,
        )

        self.chat = ChatApi(self)
        self.configuration = ConfigurationApi(self)
        self.conversations = ConversationsApi(self)
        self.events = EventsApi(self)
        self.files = FilesApi(self)
        self.interactions = InteractionsApi(self)
        self.knowledge = KnowledgeApi(self)
        self.messages = MessagesApi(self)
        self.sql = SqlApi(self)
        self.workspace = WorkspaceApi(self)

    @property
    @deprecated("low_level is retained only for migration and will be removed in 1.0")
    def low_level(self) -> AgentsUserClient:
        """返回旧通用请求入口。 / Return the deprecated generic request surface."""
        return self

    def close(self) -> None:
        """释放连接池。 / Close the underlying connection pool."""
        self._http.close()

    def __enter__(self) -> AgentsUserClient:
        return self

    def __exit__(self, exc_type: object, exc_value: object, traceback: object) -> None:
        self.close()

    def _request_model(
        self,
        method: str,
        suffix: str,
        response_type: type[ModelT],
        body: RequestBody = None,
        query: Sequence[QueryParameter] = (),
    ) -> ModelT:
        """调用 JSON 接口并解析为明确 Pydantic 模型。 / Parse JSON into one explicit model.

        Args:
            method: HTTP method。
            suffix: 已完成路径转义的 channel chat 相对路径。
            response_type: 与契约响应对应的 Pydantic 模型类。
            body: 明确的请求模型或最终 UTF-8 JSON 字符串；无请求体时省略。
            query: 保留顺序并允许重复名称的查询参数。

        Raises:
            ApiError: 服务端返回非 2xx 状态。
        """
        return response_type.model_validate_json(self._raw_response(method, suffix, body, query).content)

    @deprecated("Use the matching grouped facade operation; this helper will be removed in 1.0")
    def request_model(
        self,
        method: str,
        suffix: str,
        response_type: type[ModelT],
        body: RequestBody = None,
        query: Sequence[QueryParameter] = (),
    ) -> ModelT:
        """调用兼容期的通用 JSON 入口。 / Call the deprecated generic JSON entry point."""
        return self._request_model(method, suffix, response_type, body, query)

    def _request_status(
        self,
        method: str,
        suffix: str,
        body: RequestBody = None,
        query: Sequence[QueryParameter] = (),
    ) -> int:
        """调用无响应正文的端点并返回 2xx HTTP 状态码。 / Return the successful HTTP status."""
        return self._raw_response(method, suffix, body, query).status_code

    @deprecated("Use the matching grouped facade operation; this helper will be removed in 1.0")
    def request_status(
        self,
        method: str,
        suffix: str,
        body: RequestBody = None,
        query: Sequence[QueryParameter] = (),
    ) -> int:
        """调用兼容期的通用状态入口。 / Call the deprecated generic status entry point."""
        return self._request_status(method, suffix, body, query)

    def _request_bytes(
        self,
        method: str,
        suffix: str,
        query: Sequence[QueryParameter] = (),
        accept: str | None = None,
    ) -> bytes:
        """下载未经文本转换的二进制响应。 / Download exact response bytes.

        Args:
            method: HTTP method，通常为 `GET`。
            suffix: 已编码的相对路径。
            query: 保留顺序的查询参数。
        """
        return self._raw_response(method, suffix, query=query, accept=accept or "application/octet-stream").content

    @deprecated("Use the matching grouped facade operation; this helper will be removed in 1.0")
    def request_bytes(self, method: str, suffix: str, query: Sequence[QueryParameter] = ()) -> bytes:
        """调用兼容期的通用下载入口。 / Call the deprecated generic download entry point."""
        return self._request_bytes(method, suffix, query)

    def _raw_response(
        self,
        method: str,
        suffix: str,
        body: RequestBody = None,
        query: Sequence[QueryParameter] = (),
        accept: str = "application/json",
    ) -> httpx.Response:
        """固定最终请求内容后签名并发送。 / Sign and send the exact final request.

        每次调用重新生成 timestamp 与 nonce，不对写请求自动重试。

        Args:
            method: HTTP method。
            suffix: 已完成路径转义的相对路径，本方法不会二次编码。
            body: 明确请求模型或最终 JSON 字符串，最大 2 MiB。
            query: 最终查询参数；顺序和重复键均参与签名。
            accept: 精确 Accept 值，例如 `application/json`、`text/event-stream` 或 `text/csv`。

        Raises:
            ApiError: 服务端返回非 2xx 状态，异常不包含 secret。
        """
        request = self._signed_request(method, suffix, body, query, accept)
        response = self._http.send(request)
        if not response.is_success:
            raise ApiError(method, suffix, response.status_code, response.text)
        return response

    @deprecated("Use low_level or a grouped facade operation; this helper will be removed in 1.0")
    def raw_response(
        self,
        method: str,
        suffix: str,
        body: RequestBody = None,
        query: Sequence[QueryParameter] = (),
        accept: str = "application/json",
    ) -> httpx.Response:
        """调用兼容期的原始响应入口。 / Call the deprecated raw-response entry point."""
        return self._raw_response(method, suffix, body, query, accept)

    def _stream_chat_events(
        self,
        suffix: str,
        input: AiChatStreamInput,
        request_id: str | None = None,
    ) -> Iterator[AiChatBriefEvent]:
        """订阅对话 SSE，并返回强类型事件或 raw JSON fallback。 / Stream typed conversation events.

        Args:
            conversation_id: 要订阅的会话 ID。
            message_id: 触发本次生成的消息 ID。

        Yields:
            15 种已知事件之一；未知 type 使用包含原始 JSON 的明确 fallback。

        迭代提前结束或抛出异常时始终关闭响应流。
        """
        request = self._signed_request("POST", suffix, input, (), "text/event-stream", request_id)
        response = self._http.send(request, stream=True)
        try:
            if not response.is_success:
                response.read()
                raise ApiError("POST", suffix, response.status_code, response.text)
            for data in decode_sse_lines(response.iter_lines()):
                yield decode_ai_chat_brief_event(data)
        finally:
            response.close()

    @deprecated("Use chat.stream_chat_events(conversation_id, AiChatStreamInput(messageId=...))")
    def stream_chat_events(self, conversation_id: str, message_id: str) -> Iterator[AiChatBriefEvent]:
        """订阅兼容期的聊天事件入口。 / Use the deprecated chat-event entry point."""
        suffix = f"/conversations/{quote(conversation_id, safe='')}/stream"
        return self._stream_chat_events(suffix, AiChatStreamInput(messageId=message_id))

    def _probe_event_stream(
        self,
        suffix: str,
        input: ChatStreamProbeInput,
        request_id: str | None = None,
    ) -> Iterator[ChatStreamProbeEvent]:
        """解码诊断 SSE。 / Decode the diagnostic SSE stream."""
        request = self._signed_request("POST", suffix, input, (), "text/event-stream", request_id)
        response = self._http.send(request, stream=True)
        try:
            if not response.is_success:
                response.read()
                raise ApiError("POST", suffix, response.status_code, response.text)
            for data in decode_sse_lines(response.iter_lines()):
                yield ChatStreamProbeEvent.model_validate_json(data)
        finally:
            response.close()

    def _signed_request(
        self,
        method: str,
        suffix: str,
        body: RequestBody,
        query: Sequence[QueryParameter],
        accept: str,
        request_id: str | None = None,
    ) -> httpx.Request:
        body_text: str | None
        if isinstance(body, BaseModel):
            body_text = body.model_dump_json(by_alias=True, exclude_none=True)
        elif isinstance(body, str) or body is None:
            body_text = body
        else:
            body_text = "[" + ",".join(item.model_dump_json(by_alias=True, exclude_none=True) for item in body) + "]"
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
        if request_id is not None:
            headers["X-Request-ID"] = request_id
        return self._http.build_request(method, url, headers=headers, content=body_bytes)


def sign_canonical(secret_key: str, canonical: str) -> str:
    """计算固定规范串的 HMAC。 / Sign a deterministic canonical string.

    Args:
        secret_key: HMAC-SHA256 secret。
        canonical: 已按协议字段顺序拼接的规范字符串。

    Returns:
        小写十六进制签名。
    """
    return hmac.new(secret_key.encode("utf-8"), canonical.encode("utf-8"), hashlib.sha256).hexdigest()


# Compatibility aliases for 0.3.x callers; new code should use the unprefixed names.
LingyaAgentsClient = AgentsClient
LingyaAgentsUserClient = AgentsUserClient
LingyaApiError = ApiError
