# Lingya Agents SDK for Python

灵芽 Agents OpenAPI 的服务端 Python SDK。模型来自固定契约提交，覆盖全部 46 个公开路由，并内置 `OPENAPI-HMAC-SHA256-V1` 签名与 SSE 解码。

> 仅适用于可信服务端。不要把 secret 放入浏览器、桌面端、移动端、日志或异常。

## 安装

```bash
pip install lingya-agents-sdk
```

国内网络可使用清华镜像：

```bash
pip install lingya-agents-sdk -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## 调用

```python
from lingya_agents_sdk import LingyaAgentsClient, OpenApiCredentials
from lingya_agents_sdk.models.ai_chat_submission import AiChatSubmission

client = LingyaAgentsClient(
    "https://lingtong.lingya.tech",
    "channel-id",
    OpenApiCredentials("access-key", "secret-key"),
)
with client.for_user("your-system-user-id") as user:
    submission = user.request_model(
        "POST",
        "",
        AiChatSubmission,
        '{"query":"你好"}',
    )
    for event in user.stream_chat_events(submission.conversation_id, submission.message_id):
        print(event.type)
```

`QueryParameter` 保留参数顺序并支持重复名称。`request_model` 只接受明确的 Pydantic 返回模型；二进制下载使用 `request_bytes`。15 种已知事件和 12 种已知工具扩展均映射为明确 DTO，服务端新增判别值则以 `raw_json` 保留原始对象。

## 开发验证

```bash
python -m venv .venv
.venv/Scripts/pip install -e ".[test]" -i https://pypi.tuna.tsinghua.edu.cn/simple
.venv/Scripts/python -m ruff check lingya_agents_sdk/client.py lingya_agents_sdk/events.py lingya_agents_sdk/sse.py tests scripts
.venv/Scripts/python -m mypy
.venv/Scripts/python scripts/audit_models.py
.venv/Scripts/python -m pytest -m "not live"
.venv/Scripts/python -m build --no-isolation
```

CI 使用 `requirements-ci.txt` 固定完整依赖解析结果；依赖范围仍以 `pyproject.toml` 为发布契约。

真实测试还需要设置 `OPENAPI_AK`、`OPENAPI_SK`、`LINGYA_LIVE_BASE_URL` 与 `LINGYA_LIVE_CHANNEL_ID`，然后运行 `pytest -m live`。测试逐一核对契约中的 46 个 method/path，并在 `build/reports/live-api/` 生成脱敏报告。

契约来源：`lingya-ai/lingya-agents-openapi@7362df0`，OpenAPI Generator `7.25.0`。
