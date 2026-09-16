# 灵涯 Agents Python SDK
Lingya Agents SDK for Python

用于在 Python 可信服务端调用灵涯 Agents OpenAPI。
Use this SDK to call Lingya Agents OpenAPI from a trusted Python server.

## 安装
Installation

```bash
pip install lingya-agents-sdk==0.4.0
```

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
    print(error.status_code, error.response_body)
```

请只在可信服务端保存 `secret_key`，不要将其放入浏览器、移动端、桌面端或日志。
Keep `secret_key` on trusted servers only; never put it in browsers, mobile apps, desktop apps, or logs.
