"""Channel-binding coverage and request-path tests."""

from __future__ import annotations

import inspect
import json
import re
from pathlib import Path

import httpx

from lingya_agents_sdk import AgentsClient, OpenApiCredentials, bound_api
from lingya_agents_sdk.models.ai_chat_input import AiChatInput
from lingya_agents_sdk.models.update_conversation_group_input import UpdateConversationGroupInput


def test_every_contract_operation_has_one_bound_method() -> None:
    """Ensure the generated public surface neither drops nor duplicates an operation."""
    manifest = json.loads((Path(__file__).parents[1] / "openapi/endpoints.json").read_text(encoding="utf-8"))
    methods: set[tuple[str, str]] = set()
    for operation in manifest:
        class_name = f"Lingya{operation['group'].title()}Api"
        method_name = _snake_case(operation["operationId"])
        method = getattr(getattr(bound_api, class_name), method_name)
        assert "channel_id" not in inspect.signature(method).parameters
        methods.add((class_name, method_name))

    assert len(manifest) == 64
    assert len(methods) == 64


def test_root_channel_is_encoded_and_injected_once() -> None:
    """Verify a body-only operation cannot override the channel selected by the root client."""
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(
            201,
            json={
                "conversationId": "conversation-1",
                "messageId": "message-1",
                "disposition": "queued",
                "status": "pending",
            },
        )

    user = AgentsClient(
        "https://example.test",
        "channel/一",
        OpenApiCredentials("abcdefghijklmnopqrstuvwxyzABCDEF", "test-secret"),
    ).for_user("external-user")
    user._http.close()
    user._http = httpx.Client(transport=httpx.MockTransport(handler))
    try:
        result = user.chat.create_chat(AiChatInput(query="你好"))
    finally:
        user.close()

    assert result.message_id == "message-1"
    assert captured[0].url.raw_path.split(b"?", 1)[0] == b"/api/agents/channel/openapi/v1/channel%2F%E4%B8%80/chat"


def _snake_case(value: str) -> str:
    first = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", value)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", first).lower()


def test_explicit_null_group_is_sent_and_metadata_is_returned() -> None:
    """Ungrouping requires a present null, rather than an omitted JSON property."""
    captured: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        captured.append(request)
        return httpx.Response(
            200,
            json={
                "conversationId": "c1",
                "status": "ACTIVE",
                "title": "Title",
                "titleState": "GENERATED",
                "groupId": None,
                "groupName": None,
                "lastUpdateTime": "2026-10-20T00:00:00Z",
            },
        )

    user = AgentsClient(
        "https://example.test",
        "channel",
        OpenApiCredentials(
            "abcdefghijklmnopqrstuvwxyzABCDEF",
            "test-secret",
        ),
    ).for_user("external-user")
    user._http.close()
    user._http = httpx.Client(transport=httpx.MockTransport(handler))
    try:
        result = user.conversations.move_conversation_to_group("c1", UpdateConversationGroupInput(groupId=None))
    finally:
        user.close()
    assert json.loads(captured[0].content) == {"groupId": None}
    assert result.conversation_id == "c1"
