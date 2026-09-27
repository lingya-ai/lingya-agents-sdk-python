# Changelog

## 0.5.0 - 2026-09-27

- 同步 OpenAPI 契约 v0.1.5，新增异步任务同步及子 Agent 查询、结果和取消接口。
- 更新公开 API 封装与生成模型，使其匹配当前契约结构。

## 0.4.0

- Rename the primary API to `AgentsClient`, `AgentsUserClient`, `ApiError`, and unprefixed group facades.
- Keep the 0.3.x `Lingya*` names as compatibility aliases.
- Rewrite the README as a usage-only bilingual guide.

## 0.3.0

- Bind `channel_id` once and expose all 46 operations through generated, grouped facades.
- Keep generic HTTP helpers as deprecated compatibility APIs until 1.0.
- Generate public method signatures from contract 0.1.3 operation metadata.

## 0.1.2

- 首个 Python SDK：覆盖 46 个 Agents OpenAPI 路由、HMAC-SHA256-V1、SSE 和强类型模型。
- 15 种事件与 12 种工具扩展使用明确类型，未知判别值保留原始 JSON 字符串。
