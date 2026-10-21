# 灵涯 Agents Python SDK
Lingya Agents SDK for Python

用于在 Python 可信服务端调用灵涯 Agents OpenAPI。
Use this SDK to call Lingya Agents OpenAPI from a trusted Python server.

## 安装
Installation

```bash
pip install lingya-agents-sdk==0.7.0
```

## 一次性令牌回调

`AgentsClient` 使用同步回调，`AsyncAgentsClient` 使用异步回调；每次返回一枚新令牌，不接收外部用户 ID。
AgentsClient uses synchronous callbacks; AsyncAgentsClient uses asynchronous callbacks. Each request obtains a fresh token whose identity is bound by the issuer.

```python
from lingya_agents_sdk import AgentsClient, TokenAuth, TokenContext

# issue_fresh_token 是你的业务服务接口；签发方持有服务端 AK/SK。
def token_provider(context: TokenContext) -> str:
    return issue_fresh_token(context.channel_id)

with AgentsClient(base_url, channel_id, auth=TokenAuth(token_provider)) as client:
    submission = client.chat.create_chat(AiChatInput(query="你好"))
```

`AiChatInput` 从 `lingya_agents_sdk.models.ai_chat_input` 导入。服务端可用 `auth=HmacAuth(credentials, external_user_id)` 在构造时绑定身份，随后直接访问业务分组；原有传入 credentials 后调用 `for_user` 的方式保持兼容。选项构造已绑定身份，不能再通过 `for_user` 切换。
Import AiChatInput from its model module. HmacAuth binds credentials and an external user at construction. Legacy credential construction and for_user remain available; auth construction cannot switch users afterward.

令牌有效期十分钟，但只允许认证一次；每次请求、手动重试和 SSE/WebSocket 重新连接都独立调用回调，不缓存、不合并并发签发、不自动重试或跟随重定向。认证成功后即消费，业务失败不能复用。Token 模式不携带 HMAC 头，不能调用 `createOpenApiToken`；需由持有 AK/SK 的可信服务端签发。回调异常及非法 token 会在业务请求发出前拒绝。`/api/agents-token`、`issue_fresh_token` / `issueFreshToken` 都是业务系统示意，并非 SDK 新增接口。签发服务应从登录态确定用户和允许的渠道。
Tokens expire after ten minutes but authenticate only once. Each request, explicit retry, and SSE/WebSocket reconnection invokes the provider independently. Token clients do not cache, share issuance, retry automatically, follow redirects, send HMAC headers, or call presign. Use a trusted server to issue tokens for the authenticated business user and permitted channel; the example issuer functions/routes belong to your application.

## 快速开始
Quick start

```python
import os

from lingya_agents_sdk import AgentsClient, OpenApiCredentials
from lingya_agents_sdk.models.ai_chat_input import AiChatInput

client = AgentsClient(
    "https://lingtong.lingya.tech/",
    os.environ["OPENAPI_CHANNEL_ID"],
    OpenApiCredentials(
        os.environ["OPENAPI_AK"],
        os.environ["OPENAPI_SK"],
    ),
)

with client.for_user("external-user-id") as user:
    submission = user.chat.create_chat(AiChatInput(query="你好"))
```

`channel_id` 只在创建 `AgentsClient` 时提供，业务方法不再接收它。
Provide `channel_id` only when creating `AgentsClient`; business methods do not accept it.

## SSE 事件流
SSE event stream

```python
from lingya_agents_sdk.models.ai_chat_stream_input import AiChatStreamInput

with client.for_user("external-user-id") as user:
    for event in user.chat.stream_chat_events(
        submission.conversation_id,
        AiChatStreamInput(message_id=submission.message_id),
    ):
        print(event.type)
```

## API 分组
API groups

可用分组为 `chat`、`configuration`、`conversations`、`events`、`files`、`interactions`、`knowledge`、`messages`、`sql` 和 `workspace`。
Available groups are `chat`, `configuration`, `conversations`, `events`, `files`, `interactions`, `knowledge`, `messages`, `sql`, and `workspace`.

## 错误处理
Error handling

```python
from lingya_agents_sdk import ApiError

try:
    user.conversations.get_conversation_title("conversation-id")
except ApiError as error:
    print(error.kind, error.status_code, error.code, str(error), error.fields, error.request_id)
```

请只在可信服务端保存 `secret_key`，不要将其放入浏览器、移动端、桌面端或日志。
Keep `secret_key` on trusted servers only; never put it in browsers, mobile apps, desktop apps, or logs.


## 0.7 请求生命周期与订阅

```python
import httpx
from lingya_agents_sdk import AsyncAgentsClient, AsyncTokenAuth, RequestOptions

async with httpx.AsyncClient() as http:
    async def issue_token(context):
        response = await http.post("https://business.example/api/agents-token")
        response.raise_for_status()
        return response.json()["token"]

    async with AsyncAgentsClient(base_url, channel_id, auth=AsyncTokenAuth(issue_token), http_client=http) as client:
        await client.configuration.get_agents_config(request_options=RequestOptions(timeout_ms=5000))
        async with client.chat.subscribe_chat_events(conversation_id, input, transport="websocket") as subscription:
            async for event in subscription:
                consume(event)
        download = await client.sql.export_sql_query_result_with_metadata(conversation_id, result_id, "CSV")
```
同步客户端保留 `AgentsClient`；同步回调只能协作取消。异步任务取消使用原生 `asyncio.CancelledError`。

超时覆盖获取令牌、建连和完整响应；SDK 不自动重试或重连。业务 End 立即释放连接，WebSocket complete/1000 不补造 End。错误包含可判别分类、HTTP 状态和可取得的业务错误及请求标识。详见 [生命周期、错误和生成机制](docs/request-lifecycle.md)。运行时由契约项目统一生成，修改生成产物会被 CI 检出。
