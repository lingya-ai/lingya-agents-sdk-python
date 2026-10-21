"""Single-use token transport regression tests."""

from concurrent.futures import ThreadPoolExecutor
from threading import Lock

import httpx
import pytest

from lingya_agents_sdk import AgentsClient, ApiError, HmacAuth, OpenApiCredentials, TokenAuth, TokenContext
from lingya_agents_sdk.models.ai_chat_input import AiChatInput
from lingya_agents_sdk.models.chat_stream_probe_input import ChatStreamProbeInput


def test_concurrent_requests_get_independent_tokens_and_reject_presign() -> None:
    issued = 0
    lock = Lock()
    requests: list[httpx.Request] = []

    def provider(context: TokenContext) -> str:
        nonlocal issued
        assert context.channel_id == "channel"
        with lock:
            issued += 1
            return f"fresh-{issued}"

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(
            201,
            json={
                "conversationId": "conversation",
                "messageId": "message",
                "disposition": "queued",
                "status": "pending",
            },
        )

    with AgentsClient("https://example.test", "channel", auth=TokenAuth(provider)) as client:
        client._user()._http.close()
        client._user()._http = httpx.Client(transport=httpx.MockTransport(handler))
        with ThreadPoolExecutor(max_workers=2) as pool:
            list(pool.map(lambda _: client.chat.create_chat(AiChatInput(query="hello")), range(2)))
        assert issued == 2
        assert {r.headers["X-OpenAPI-Token"] for r in requests} == {"fresh-1", "fresh-2"}
        for request in requests:
            assert [h for h in request.headers if h.startswith("x-openapi-")] == ["x-openapi-token"]
        with pytest.raises(ApiError, match="presign requires HMAC"):
            client.configuration.create_open_api_token()
        with pytest.raises(ValueError, match="already binds"):
            client.for_user("other")
        assert issued == 2


@pytest.mark.parametrize("token", ["", "secret\r\nheader", "invalid token", "中文"])
def test_invalid_token_never_sends(token: str) -> None:
    with AgentsClient("https://example.test", "channel", auth=TokenAuth(lambda _: token)) as client:
        with pytest.raises(ApiError, match="Invalid OpenAPI token"):
            client.chat.create_chat(AiChatInput(query="hello"))


def test_callback_error_is_redacted_and_401_is_not_retried() -> None:
    def fail(_: TokenContext) -> str:
        raise RuntimeError("secret-token")

    with AgentsClient("https://example.test", "channel", auth=TokenAuth(fail)) as client:
        with pytest.raises(ApiError, match="^OpenAPI token provider failed$"):
            client.chat.create_chat(AiChatInput(query="hello"))

    issued = 0

    def provider(_: TokenContext) -> str:
        nonlocal issued
        issued += 1
        return f"fresh-{issued}"

    with AgentsClient("https://example.test", "channel", auth=TokenAuth(provider)) as client:
        client._user()._http.close()
        client._user()._http = httpx.Client(transport=httpx.MockTransport(lambda _: httpx.Response(401, json={})))
        for count in range(1, 3):
            with pytest.raises(ApiError):
                client.chat.create_chat(AiChatInput(query="hello"))
            assert issued == count


def test_hmac_options_bind_identity() -> None:
    with AgentsClient(
        "https://example.test", "channel", auth=HmacAuth(OpenApiCredentials("access", "secret"), "user")
    ) as client:

        def handler(request: httpx.Request) -> httpx.Response:
            assert request.headers["X-OpenAPI-AK"] == "access"
            assert request.headers["X-OpenAPI-User"] == "dXNlcg"
            assert "X-OpenAPI-Token" not in request.headers
            return httpx.Response(
                201,
                json={
                    "conversationId": "conversation",
                    "messageId": "message",
                    "disposition": "queued",
                    "status": "pending",
                },
            )

        client._user()._http.close()
        client._user()._http = httpx.Client(transport=httpx.MockTransport(handler))
        client.chat.create_chat(AiChatInput(query="hello"))


def test_sse_gets_one_token_per_connection_and_redirects_are_not_followed() -> None:
    issued = 0

    def provider(_: TokenContext) -> str:
        nonlocal issued
        issued += 1
        return f"fresh-{issued}"

    requests: list[httpx.Request] = []

    def handler(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        if request.headers.get("Accept") == "text/event-stream":
            return httpx.Response(
                200,
                text=(
                    'data: {"probeId":"probe","sequence":1,"serverElapsedMs":0}\n\n'
                    'data: {"probeId":"probe","sequence":2,"serverElapsedMs":1}\n\n'
                ),
                headers={"Content-Type": "text/event-stream"},
            )
        return httpx.Response(302, headers={"Location": "https://example.test/redirect"})

    with AgentsClient("https://example.test", "channel", auth=TokenAuth(provider)) as client:
        client._user()._http.close()
        client._user()._http = httpx.Client(transport=httpx.MockTransport(handler))
        for expected in range(1, 3):
            events = client.chat.probe_event_stream(ChatStreamProbeInput(probeId="probe"))
            assert issued == expected - 1
            assert len(list(events)) == 2
            assert issued == expected
        with pytest.raises(ApiError):
            client.chat.create_chat(AiChatInput(query="hello"))
        assert len(requests) == 3
        assert issued == 3
