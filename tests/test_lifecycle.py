import asyncio
import json
import threading
from pathlib import Path

import httpx
import pytest

from lingya_agents_sdk import AgentsClient, ApiError, AsyncAgentsClient, AsyncTokenAuth, RequestOptions, TokenAuth
from lingya_agents_sdk.models.ai_chat_stream_input import AiChatStreamInput


def test_async_token_timeout_and_native_cancellation():
    async def run():
        sends = 0

        async def network(request):
            nonlocal sends
            sends += 1
            return httpx.Response(200, json={})

        async def token(context):
            await asyncio.Event().wait()
            return "never"

        async with httpx.AsyncClient(transport=httpx.MockTransport(network)) as http:
            async with AsyncAgentsClient(
                "https://example.test", "c", auth=AsyncTokenAuth(token), http_client=http
            ) as client:
                with pytest.raises(ApiError) as error:
                    await client.configuration.get_agents_config(request_options=RequestOptions(timeout_ms=10))
                assert error.value.kind == "timeout"
                task = asyncio.create_task(client.configuration.get_agents_config())
                await asyncio.sleep(0)
                task.cancel()
                with pytest.raises(asyncio.CancelledError):
                    await task
                assert sends == 0
            assert not http.is_closed

    asyncio.run(run())


def test_late_async_token_is_discarded_when_provider_ignores_cancellation():
    async def run():
        release = asyncio.Event()
        sends = 0

        async def token(context):
            try:
                await release.wait()
            except asyncio.CancelledError:
                await release.wait()
            return "late"

        async def network(request):
            nonlocal sends
            sends += 1
            return httpx.Response(200, json={})

        async with httpx.AsyncClient(transport=httpx.MockTransport(network)) as http:
            async with AsyncAgentsClient("https://example.test", "c", auth=AsyncTokenAuth(token), http_client=http) as client:
                with pytest.raises(ApiError) as error:
                    await asyncio.wait_for(client.configuration.get_agents_config(request_options=RequestOptions(timeout_ms=10)), 0.5)
                assert error.value.kind == "timeout"
                release.set()
                await asyncio.sleep(0.02)
                assert sends == 0

    asyncio.run(run())


def test_async_cancel_event_interrupts_token_and_explicit_close_interrupts_read():
    async def run():
        async def token(context):
            await asyncio.Event().wait()
            return "late"

        cancelled = threading.Event()
        async with AsyncAgentsClient("https://example.test", "c", auth=AsyncTokenAuth(token)) as client:
            task = asyncio.create_task(client.configuration.get_agents_config(request_options=RequestOptions(cancel_event=cancelled)))
            await asyncio.sleep(0.02)
            cancelled.set()
            with pytest.raises(ApiError) as error:
                await asyncio.wait_for(task, 1)
            assert error.value.kind == "cancelled"
            sub = client.chat.subscribe_chat_events("c", AiChatStreamInput(messageId="m"))
            read = asyncio.create_task(sub.__anext__())
            await asyncio.sleep(0.02)
            await asyncio.wait_for(sub.aclose(), 1)
            with pytest.raises(asyncio.CancelledError):
                await read
            assert (await sub.closed)["reason"] == "closed"

    asyncio.run(run())


def test_async_websocket_uses_fresh_subprotocol_and_preserves_unknown_events():
    from websockets.asyncio.server import serve

    async def run():
        issued = 0
        protocols = []
        diagnostics = []
        options = RequestOptions(timeout_ms=2000, on_connection_event=diagnostics.append)

        def response_header(connection, request, response):
            response.headers["X-Request-ID"] = "server-ws"
            return response

        async def token(context):
            nonlocal issued
            issued += 1
            return f"fresh-{issued}"

        async def peer(socket):
            protocols.append(socket.request.headers["Sec-WebSocket-Protocol"])
            for event in [{"event": "ready"}, {"event": "future", "data": {"type": "future", "kept": True}}, {"event": "complete"}]:
                await socket.send(json.dumps({"id": "m", **event}))
            await socket.wait_closed()

        async with serve(peer, "127.0.0.1", 0, process_response=response_header) as server:
            port = server.sockets[0].getsockname()[1]
            async with AsyncAgentsClient(f"http://127.0.0.1:{port}", "c", auth=AsyncTokenAuth(token)) as client:
                for _ in range(2):
                    sub = client.chat.subscribe_chat_events("c", AiChatStreamInput(messageId="m"), transport="websocket", request_options=options)
                    assert [event.type async for event in sub] == ["future"]
                    assert (await sub.closed)["reason"] == "complete"
            assert protocols == ["xlt-openapi-token.fresh-1", "xlt-openapi-token.fresh-2"]
            opened = [event for event in diagnostics if event["type"] == "opened"]
            closed = [event for event in diagnostics if event["type"] == "closed"]
            assert len(opened) == len(closed) == 2
            assert len({event["connection_id"] for event in opened}) == 2
            assert all(event["request_id"] == "server-ws" for event in opened + closed)
            assert [event["connection_id"] for event in opened] == [event["connection_id"] for event in closed]

    asyncio.run(run())


def test_sync_http_errors_and_download_metadata():
    def network(request):
        if request.url.path.endswith("/export"):
            return httpx.Response(
                200,
                content=bytes([0, 255]),
                headers={
                    "Content-Disposition": "attachment; filename*=UTF-8''%E4%B8%AD.csv",
                    "Content-Type": "text/csv",
                },
            )
        return httpx.Response(
            410,
            json={"code": "EXPIRED", "message": "expired", "fields": [{"field": "title", "message": "required"}]},
            headers={"X-Request-ID": "server"},
        )

    with httpx.Client(transport=httpx.MockTransport(network)) as http:
        with AgentsClient("https://example.test", "c", auth=TokenAuth(lambda _: "fresh"), http_client=http) as client:
            with pytest.raises(ApiError) as error:
                client.configuration.get_agents_config()
            assert (error.value.kind, error.value.code, error.value.request_id) == ("http", "EXPIRED", "server")
            result = client.sql.export_sql_query_result_with_metadata("c", "r", "CSV")
            assert result.filename == "中.csv" and result.bytes == bytes([0, 255])
        assert not http.is_closed


def test_async_end_and_unexpected_eof():
    async def run():
        ended = False

        class Body(httpx.AsyncByteStream):
            async def __aiter__(self):
                yield (
                    "data: "
                    + json.dumps(
                        {
                            "type": "end",
                            "executionTimeMillis": 0,
                            "totalUsage": {"inputTokens": 0, "outputTokens": 0, "totalTokens": 0},
                            "artifacts": [],
                            "nonFileArtifacts": [],
                        }
                    )
                    + "\n\n"
                ).encode()
                await asyncio.Event().wait()

            async def aclose(self):
                nonlocal ended
                ended = True

        async def token(context):
            return "fresh"

        async with httpx.AsyncClient(
            transport=httpx.MockTransport(
                lambda req: httpx.Response(200, stream=Body(), headers={"Content-Type": "text/event-stream"})
            )
        ) as http:
            async with AsyncAgentsClient(
                "https://example.test", "c", auth=AsyncTokenAuth(token), http_client=http
            ) as client:
                events = [
                    event async for event in client.chat.stream_chat_events("c", AiChatStreamInput(messageId="m"))
                ]
                assert [event.type for event in events] == ["end"] and ended

    asyncio.run(run())


def test_shared_http_error_vectors():
    vectors = json.loads((Path(__file__).parents[1] / "test-vectors/lifecycle-v1.json").read_text(encoding="utf8"))
    for vector in vectors["httpErrors"]:
        def network(request):
            return httpx.Response(vector["status"], json=vector["body"], headers={"X-Request-ID": vector["requestId"]})
        with httpx.Client(transport=httpx.MockTransport(network)) as http:
            with AgentsClient("https://example.test", "c", auth=TokenAuth(lambda _: "fresh"), http_client=http) as client:
                with pytest.raises(ApiError) as error:
                    client.configuration.get_agents_config()
                assert error.value.status_code == vector["status"]
                assert error.value.code == vector["body"]["code"]
                assert error.value.fields[0]["field"] == "title"
                assert error.value.request_id == vector["requestId"]
