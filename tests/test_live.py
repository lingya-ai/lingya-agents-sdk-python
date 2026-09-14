"""Real-service coverage for every published operation."""

from __future__ import annotations

import json
import os
import re
import uuid
from dataclasses import dataclass
from pathlib import Path

import pytest

from lingya_agents_sdk.client import (
    LingyaAgentsClient,
    LingyaAgentsUserClient,
    LingyaApiError,
    OpenApiCredentials,
    QueryParameter,
)
from lingya_agents_sdk.models.ai_chat_submission import AiChatSubmission
from lingya_agents_sdk.models.conversation_share_created import ConversationShareCreated
from lingya_agents_sdk.models.generate_pre_signed_url_output import GeneratePreSignedUrlOutput
from lingya_agents_sdk.sse import decode_sse_lines

BASE_PATH = "/api/agents/channel/openapi/v1/{channelId}/chat"
DOMAIN_STATUSES = {400, 403, 404, 409, 422}


@dataclass(frozen=True)
class Result:
    method: str
    path: str
    status: int
    outcome: str
    request_id: str


@pytest.mark.live
def test_all_46_real_endpoints() -> None:
    names = ("OPENAPI_AK", "OPENAPI_SK", "LINGYA_LIVE_BASE_URL", "LINGYA_LIVE_CHANNEL_ID")
    if any(not os.getenv(name) for name in names):
        pytest.skip("live environment variables are required")
    client = LingyaAgentsClient(
        os.environ["LINGYA_LIVE_BASE_URL"],
        os.environ["LINGYA_LIVE_CHANNEL_ID"],
        OpenApiCredentials(os.environ["OPENAPI_AK"], os.environ["OPENAPI_SK"]),
    )
    with client.for_user(os.getenv("LINGYA_LIVE_EXTERNAL_USER_ID", "lingya-python-sdk-all-endpoints")) as user:
        coverage = Coverage(user)
        first = coverage.model("POST", "", AiChatSubmission, {"query": "仅回复英文 OK"})
        try:
            coverage.success("GET", "/config")
            events = list(user.stream_chat_events(first.conversation_id, first.message_id))
            assert events and any(getattr(event, "type", None) == "end" for event in events)
            coverage.record("POST", "/conversations/{conversationId}/stream", 200, "流式响应完成")
            coverage.success("GET", f"/conversations/{first.conversation_id}/config")
            coverage.success("GET", f"/conversations/{first.conversation_id}/context-usage")
            coverage.success(
                "GET", "/conversations", query=[QueryParameter("current", "0"), QueryParameter("size", "5")]
            )
            coverage.success("GET", "/conversations/active")
            coverage.success("GET", "/conversations/unread")
            coverage.success("POST", "/conversations/activity/query", {"conversationIds": [first.conversation_id]})
            coverage.success(
                "PUT", f"/conversations/{first.conversation_id}/read-receipt", {"messageId": first.message_id}
            )
            coverage.success("GET", "/conversations/stats")
            coverage.success(
                "PATCH", f"/conversations/{first.conversation_id}/title", {"title": "Python SDK 全接口测试"}
            )
            coverage.success("GET", f"/conversations/{first.conversation_id}/title")
            coverage.success("GET", f"/conversations/{first.conversation_id}/messages")
            coverage.success("GET", f"/conversations/{first.conversation_id}/messages/{first.message_id}")
            coverage.success(
                "GET",
                "/events",
                query=[
                    QueryParameter("conversationId", first.conversation_id),
                    QueryParameter("messageId", first.message_id),
                ],
            )
            coverage.success(
                "POST", "/events/batch", {"conversationId": first.conversation_id, "messageIds": [first.message_id]}
            )
            second = coverage.model(
                "POST", f"/conversations/{first.conversation_id}", AiChatSubmission, {"query": "再次仅回复英文 OK"}
            )
            list(user.stream_chat_events(second.conversation_id, second.message_id))
            coverage.success("DELETE", f"/conversations/{first.conversation_id}/interrupt")
            coverage.success("POST", f"/conversations/{first.conversation_id}/compact")
            coverage.success("GET", f"/conversations/{first.conversation_id}/async-tasks")
            coverage.domain("GET", f"/conversations/{first.conversation_id}/async-tasks/missing-async-task")
            coverage.domain("DELETE", f"/conversations/{first.conversation_id}/messages/{first.message_id}/queue")
            share = coverage.model(
                "POST", f"/conversations/{first.conversation_id}/shares", ConversationShareCreated, {}
            )
            coverage.success("GET", f"/conversations/{first.conversation_id}/shares")
            coverage.success("DELETE", f"/conversations/{first.conversation_id}/shares/{share.share_id}")
            coverage.success(
                "POST",
                "/plan/approve",
                {"conversationId": first.conversation_id, "messageId": first.message_id, "approved": False},
            )
            coverage.success("GET", "/plan/missing-plan/status")
            coverage.success(
                "GET",
                "/user-input/missing-question/status",
                query=[
                    QueryParameter("conversationId", first.conversation_id),
                    QueryParameter("messageId", first.message_id),
                ],
            )
            coverage.success(
                "POST",
                "/user-input/answer",
                {
                    "conversationId": first.conversation_id,
                    "messageId": first.message_id,
                    "questionId": "missing-question",
                    "selectedOptions": [],
                    "customInput": "not pending",
                },
            )
            coverage.domain("GET", f"/conversations/{first.conversation_id}/sql-query-results/missing-result")
            coverage.domain(
                "GET", f"/conversations/{first.conversation_id}/sql-query-results/missing-result/chart-data"
            )
            coverage.domain(
                "GET",
                f"/conversations/{first.conversation_id}/sql-query-results/missing-result/export",
                query=[QueryParameter("format", "CSV")],
                accept="text/csv",
            )
            md5 = "17/2WOZXDPjhZzwMQCHrDg=="
            coverage.success("GET", "/files/meta/contentMd5", query=[QueryParameter("contentMd5", md5)])
            upload = coverage.model(
                "POST",
                "/files/pre-signed-url/write",
                GeneratePreSignedUrlOutput,
                {"fileName": "lingya-sdk-endpoint-test.txt", "module": "ai-chat-attachments", "contentMd5": md5},
            )
            coverage.domain("POST", "/files/pre-signed-url/confirm", {"fileUk": upload.file_uk, "contentMd5": md5})
            coverage.domain(
                "POST", "/files/contentMd5", {"fileName": "lingya-sdk-endpoint-test.txt", "contentMd5": md5}
            )
            coverage.domain("GET", f"/conversations/{first.conversation_id}/files/9223372036854775807/preview")
            coverage.domain(
                "GET",
                f"/conversations/{first.conversation_id}/messages/{first.message_id}/plan-intermediate-files/9223372036854775807/preview",
            )
            coverage.success("POST", "/knowledge-bases/citations/metadata", [])
            coverage.domain("GET", "/knowledge-bases/citations/CHUNK/9223372036854775807/metadata")
            coverage.success("GET", f"/conversations/{first.conversation_id}/workspace/files")
            coverage.domain(
                "GET",
                f"/conversations/{first.conversation_id}/workspace/files/preview",
                query=[QueryParameter("path", "missing-file.txt")],
            )
            probe = user.raw_response(
                "POST", "/stream-probe", json.dumps({"probeId": f"all-{uuid.uuid4()}"}), accept="text/event-stream"
            )
            assert len(list(decode_sse_lines(probe.text.splitlines()))) == 4
            coverage.record("POST", "/stream-probe", probe.status_code, "流式响应完成")
            coverage.success("PATCH", f"/conversations/{first.conversation_id}/status", {"status": "ARCHIVED"})
        finally:
            try:
                coverage.success("DELETE", f"/conversations/{first.conversation_id}")
            finally:
                coverage.write_report()
        assert len(coverage.seen) == 46
        assert sorted(coverage.seen) == sorted(published_endpoints())


class Coverage:
    def __init__(self, user: LingyaAgentsUserClient) -> None:
        self.user = user
        self.results: list[Result] = []
        self.seen: set[str] = set()

    def success(
        self, method: str, suffix: str, body: object | None = None, query: list[QueryParameter] | None = None
    ) -> None:
        response = self.user.raw_response(
            method,
            suffix,
            json.dumps(body, separators=(",", ":"), ensure_ascii=False) if body is not None else None,
            query or [],
        )
        self.record(method, suffix, response.status_code, "通过", response)

    def model(self, method: str, suffix: str, model_type: type, body: object) -> object:
        response = self.user.raw_response(method, suffix, json.dumps(body, separators=(",", ":"), ensure_ascii=False))
        self.record(method, suffix, response.status_code, "通过", response)
        return model_type.model_validate_json(response.content)

    def domain(
        self,
        method: str,
        suffix: str,
        body: object | None = None,
        query: list[QueryParameter] | None = None,
        accept: str = "application/json",
    ) -> None:
        with pytest.raises(LingyaApiError) as caught:
            self.user.raw_response(
                method,
                suffix,
                json.dumps(body, separators=(",", ":"), ensure_ascii=False) if body is not None else None,
                query or [],
                accept,
            )
        assert caught.value.status_code in DOMAIN_STATUSES
        self.record(method, suffix, caught.value.status_code, "环境能力受限，参数与错误响应已验证")

    def record(self, method: str, suffix: str, status: int, outcome: str, response: object | None = None) -> None:
        path = BASE_PATH + canonical_suffix(suffix)
        key = f"{method} {path}"
        assert key not in self.seen
        self.seen.add(key)
        request_id = f"local-{len(self.results) + 1:03d}"
        self.results.append(Result(method, path, status, outcome, request_id))

    def write_report(self) -> None:
        directory = Path("build/reports/live-api")
        directory.mkdir(parents=True, exist_ok=True)
        rows = "\n".join(
            f"| {item.request_id} | {item.method} | `{item.path}` | {item.status} | {item.outcome} |"
            for item in self.results
        )
        (directory / "all-endpoints.md").write_text(
            f"# Python SDK 真实环境全接口测试报告\n\n| 请求标识 | Method | Path | HTTP | 结果 |\n|---|---|---|---:|---|\n{rows}\n",
            encoding="utf-8",
        )


def canonical_suffix(suffix: str) -> str:
    suffix = re.sub(
        r"^/conversations/(?!active(?:/|$)|unread(?:/|$)|stats(?:/|$)|activity(?:/|$))[^/]+",
        "/conversations/{conversationId}",
        suffix,
    )
    for pattern, replacement in [
        (r"/async-tasks/[^/]+", "/async-tasks/{asyncTaskId}"),
        (r"/messages/[^/]+", "/messages/{messageId}"),
        (r"/plan-intermediate-files/[^/]+", "/plan-intermediate-files/{fileId}"),
        (r"^/conversations/\{conversationId\}/files/[^/]+", "/conversations/{conversationId}/files/{fileId}"),
        (r"/shares/[^/]+", "/shares/{shareId}"),
        (r"/sql-query-results/[^/]+", "/sql-query-results/{resultId}"),
        (r"^/plan/[^/]+/status$", "/plan/{planId}/status"),
        (r"^/user-input/[^/]+/status$", "/user-input/{questionId}/status"),
        (
            r"^/knowledge-bases/citations/[^/]+/[^/]+/metadata$",
            "/knowledge-bases/citations/{citationType}/{referenceId}/metadata",
        ),
    ]:
        suffix = re.sub(pattern, replacement, suffix)
    return suffix


def published_endpoints() -> list[str]:
    yaml = (Path(__file__).parents[2] / "lingya-agents-openapi/openapi/lingya-agents-v1.yaml").read_text(
        encoding="utf-8"
    )
    endpoints: list[str] = []
    path = ""
    for line in yaml.splitlines():
        match = re.fullmatch(r"  (/api/agents/channel/openapi/[^:]+):", line)
        if match:
            path = match.group(1)
        method = re.fullmatch(r"    (get|post|put|patch|delete):", line)
        if method and path:
            endpoints.append(f"{method.group(1).upper()} {path}")
    return endpoints
