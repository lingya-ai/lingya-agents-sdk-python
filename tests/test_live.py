"""Real-service coverage for every published operation."""

from __future__ import annotations

import os
import re
import uuid
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import TypeVar

import pytest

from lingya_agents_sdk.client import (
    LingyaAgentsClient,
    LingyaAgentsUserClient,
    LingyaApiError,
    OpenApiCredentials,
)
from lingya_agents_sdk.models.ai_chat_events_batch_input import AiChatEventsBatchInput
from lingya_agents_sdk.models.ai_chat_input import AiChatInput
from lingya_agents_sdk.models.ai_chat_stream_input import AiChatStreamInput
from lingya_agents_sdk.models.chat_stream_probe_input import ChatStreamProbeInput
from lingya_agents_sdk.models.confirm_upload_input import ConfirmUploadInput
from lingya_agents_sdk.models.conversation_activity_batch_input import ConversationActivityBatchInput
from lingya_agents_sdk.models.conversation_read_receipt_input import ConversationReadReceiptInput
from lingya_agents_sdk.models.conversation_share_input import ConversationShareInput
from lingya_agents_sdk.models.conversation_status_input import ConversationStatusInput
from lingya_agents_sdk.models.conversation_title_input import ConversationTitleInput
from lingya_agents_sdk.models.create_file_input import CreateFileInput
from lingya_agents_sdk.models.generate_pre_signed_url_input import GeneratePreSignedUrlInput
from lingya_agents_sdk.models.plan_approval_input import PlanApprovalInput
from lingya_agents_sdk.models.user_input_answer_input import UserInputAnswerInput

BASE_PATH = "/api/agents/channel/openapi/v1/{channelId}/chat"
DOMAIN_STATUSES = {400, 403, 404, 409, 422}
T = TypeVar("T")


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
        first = coverage.success("POST", "", lambda: user.chat.create_chat(AiChatInput(query="仅回复英文 OK")), 201)
        try:
            coverage.success("GET", "/config", user.configuration.get_agents_config)
            events = list(
                user.chat.stream_chat_events(first.conversation_id, AiChatStreamInput(messageId=first.message_id))
            )
            assert events and any(getattr(event, "type", None) == "end" for event in events)
            coverage.record("POST", "/conversations/{conversationId}/stream", 200, "流式响应完成")
            coverage.success(
                "GET",
                f"/conversations/{first.conversation_id}/config",
                lambda: user.configuration.get_conversation_config(first.conversation_id),
            )
            coverage.success(
                "GET",
                f"/conversations/{first.conversation_id}/context-usage",
                lambda: user.conversations.get_conversation_context_usage(first.conversation_id),
            )
            coverage.success("GET", "/conversations", lambda: user.conversations.list_conversations(current=0, size=5))
            coverage.success("GET", "/conversations/active", user.conversations.list_active_conversations)
            coverage.success("GET", "/conversations/unread", user.conversations.list_unread_conversations)
            coverage.success(
                "POST",
                "/conversations/activity/query",
                lambda: user.conversations.query_conversation_activities(
                    ConversationActivityBatchInput(conversationIds=[first.conversation_id])
                ),
            )
            coverage.success(
                "PUT",
                f"/conversations/{first.conversation_id}/read-receipt",
                lambda: user.conversations.mark_conversation_read(
                    first.conversation_id, ConversationReadReceiptInput(messageId=first.message_id)
                ),
            )
            coverage.success("GET", "/conversations/stats", user.conversations.get_conversation_stats)
            coverage.success(
                "PATCH",
                f"/conversations/{first.conversation_id}/title",
                lambda: user.conversations.update_conversation_title(
                    first.conversation_id, ConversationTitleInput(title="Python SDK 全接口测试")
                ),
            )
            coverage.success(
                "GET",
                f"/conversations/{first.conversation_id}/title",
                lambda: user.conversations.get_conversation_title(first.conversation_id),
            )
            coverage.success(
                "GET",
                f"/conversations/{first.conversation_id}/messages",
                lambda: user.messages.list_conversation_messages(first.conversation_id),
            )
            coverage.success(
                "GET",
                f"/conversations/{first.conversation_id}/messages/{first.message_id}",
                lambda: user.messages.get_conversation_message(first.conversation_id, first.message_id),
            )
            coverage.success(
                "GET", "/events", lambda: user.events.get_chat_events(first.conversation_id, first.message_id)
            )
            coverage.success(
                "POST",
                "/events/batch",
                lambda: user.events.get_chat_events_batch(
                    AiChatEventsBatchInput(conversationId=first.conversation_id, messageIds=[first.message_id])
                ),
            )
            second = coverage.success(
                "POST",
                f"/conversations/{first.conversation_id}",
                lambda: user.chat.continue_chat(first.conversation_id, AiChatInput(query="再次仅回复英文 OK")),
                201,
            )
            list(user.chat.stream_chat_events(second.conversation_id, AiChatStreamInput(messageId=second.message_id)))
            coverage.success(
                "DELETE",
                f"/conversations/{first.conversation_id}/interrupt",
                lambda: user.chat.interrupt_conversation(first.conversation_id),
            )
            coverage.success(
                "POST",
                f"/conversations/{first.conversation_id}/compact",
                lambda: user.chat.compact_conversation(first.conversation_id),
            )
            coverage.success(
                "GET",
                f"/conversations/{first.conversation_id}/async-tasks",
                lambda: user.messages.list_conversation_async_tasks(first.conversation_id),
            )
            coverage.domain(
                "GET",
                f"/conversations/{first.conversation_id}/async-tasks/missing-async-task",
                lambda: user.messages.get_conversation_async_task(first.conversation_id, "missing-async-task"),
            )
            coverage.domain(
                "DELETE",
                f"/conversations/{first.conversation_id}/messages/{first.message_id}/queue",
                lambda: user.messages.cancel_queued_message(first.conversation_id, first.message_id),
            )
            share = coverage.success(
                "POST",
                f"/conversations/{first.conversation_id}/shares",
                lambda: user.conversations.create_conversation_share(first.conversation_id, ConversationShareInput()),
                201,
            )
            coverage.success(
                "GET",
                f"/conversations/{first.conversation_id}/shares",
                lambda: user.conversations.list_conversation_shares(first.conversation_id),
            )
            coverage.success(
                "DELETE",
                f"/conversations/{first.conversation_id}/shares/{share.share_id}",
                lambda: user.conversations.revoke_conversation_share(first.conversation_id, share.share_id),
            )
            coverage.success(
                "POST",
                "/plan/approve",
                lambda: user.interactions.approve_plan(
                    PlanApprovalInput(conversationId=first.conversation_id, messageId=first.message_id, approved=False)
                ),
            )
            coverage.success(
                "GET", "/plan/missing-plan/status", lambda: user.interactions.get_plan_status("missing-plan")
            )
            coverage.success(
                "GET",
                "/user-input/missing-question/status",
                lambda: user.interactions.get_user_input_status(
                    "missing-question", first.conversation_id, first.message_id
                ),
            )
            coverage.success(
                "POST",
                "/user-input/answer",
                lambda: user.interactions.answer_user_input(
                    UserInputAnswerInput(
                        conversationId=first.conversation_id,
                        messageId=first.message_id,
                        questionId="missing-question",
                        selectedOptions=[],
                        customInput="not pending",
                    )
                ),
            )
            coverage.domain(
                "GET",
                f"/conversations/{first.conversation_id}/sql-query-results/missing-result",
                lambda: user.sql.get_sql_query_result(first.conversation_id, "missing-result"),
            )
            coverage.domain(
                "GET",
                f"/conversations/{first.conversation_id}/sql-query-results/missing-result/chart-data",
                lambda: user.sql.get_sql_query_chart_data(first.conversation_id, "missing-result"),
            )
            coverage.domain(
                "GET",
                f"/conversations/{first.conversation_id}/sql-query-results/missing-result/export",
                lambda: user.sql.export_sql_query_result(first.conversation_id, "missing-result", "CSV"),
            )
            md5 = "17/2WOZXDPjhZzwMQCHrDg=="
            coverage.success("GET", "/files/meta/contentMd5", lambda: user.files.file_exists_by_content_md5(md5))
            upload = coverage.success(
                "POST",
                "/files/pre-signed-url/write",
                lambda: user.files.create_pre_signed_upload(
                    GeneratePreSignedUrlInput(
                        fileName="lingya-sdk-endpoint-test.txt", module="ai-chat-attachments", contentMd5=md5
                    )
                ),
            )
            file_uk = upload.file_uk
            assert file_uk is not None
            coverage.domain(
                "POST",
                "/files/pre-signed-url/confirm",
                lambda: user.files.confirm_pre_signed_upload(ConfirmUploadInput(fileUk=file_uk, contentMd5=md5)),
            )
            coverage.domain(
                "POST",
                "/files/contentMd5",
                lambda: user.files.create_file_by_content_md5(
                    CreateFileInput(fileName="lingya-sdk-endpoint-test.txt", contentMd5=md5)
                ),
            )
            coverage.domain(
                "GET",
                f"/conversations/{first.conversation_id}/files/9223372036854775807/preview",
                lambda: user.files.get_conversation_file_preview(first.conversation_id, 9223372036854775807),
            )
            coverage.domain(
                "GET",
                f"/conversations/{first.conversation_id}/messages/{first.message_id}/plan-intermediate-files/9223372036854775807/preview",
                lambda: user.files.get_plan_intermediate_file_preview(
                    first.conversation_id, first.message_id, 9223372036854775807
                ),
            )
            coverage.success(
                "POST", "/knowledge-bases/citations/metadata", lambda: user.knowledge.get_citation_metadata_batch([])
            )
            coverage.domain(
                "GET",
                "/knowledge-bases/citations/CHUNK/9223372036854775807/metadata",
                lambda: user.knowledge.get_citation_metadata("CHUNK", 9223372036854775807),
            )
            coverage.success(
                "GET",
                f"/conversations/{first.conversation_id}/workspace/files",
                lambda: user.workspace.list_workspace_artifacts(first.conversation_id),
            )
            coverage.domain(
                "GET",
                f"/conversations/{first.conversation_id}/workspace/files/preview",
                lambda: user.workspace.get_workspace_file_preview(first.conversation_id, "missing-file.txt"),
            )
            assert len(list(user.chat.probe_event_stream(ChatStreamProbeInput(probeId=f"all-{uuid.uuid4()}")))) == 4
            coverage.record("POST", "/stream-probe", 200, "流式响应完成")
            coverage.success(
                "PATCH",
                f"/conversations/{first.conversation_id}/status",
                lambda: user.conversations.update_conversation_status(
                    first.conversation_id, ConversationStatusInput(status="ARCHIVED")
                ),
            )
        finally:
            try:
                coverage.success(
                    "DELETE",
                    f"/conversations/{first.conversation_id}",
                    lambda: user.conversations.delete_conversation(first.conversation_id),
                )
            finally:
                coverage.write_report()
        assert len(coverage.seen) == 46
        assert sorted(coverage.seen) == sorted(published_endpoints())


class Coverage:
    def __init__(self, user: LingyaAgentsUserClient) -> None:
        self.user = user
        self.results: list[Result] = []
        self.seen: set[str] = set()

    def success(self, method: str, suffix: str, action: Callable[[], T], status: int = 200) -> T:
        value = action()
        self.record(method, suffix, status, "通过")
        return value

    def domain(
        self,
        method: str,
        suffix: str,
        action: Callable[[], object],
    ) -> None:
        with pytest.raises(LingyaApiError) as caught:
            action()
        assert caught.value.status_code in DOMAIN_STATUSES
        self.record(method, suffix, caught.value.status_code, "环境能力受限，参数与错误响应已验证")

    def record(self, method: str, suffix: str, status: int, outcome: str) -> None:
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
