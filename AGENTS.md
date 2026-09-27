# Python SDK 发布指南

## 契约同步

先确认 `lingya-agents-openapi` 已发布所需的 `vX.Y.Z`，再同步 `openapi/lingya-agents-v1.yaml`、`openapi/endpoints.json` 和 `CONTRACT_VERSION`。将 CI 与 release workflow 的契约引用更新到同一 tag。生成模型和 `bound_api.py` 应从契约生成；不要手工改协议字段。

## 版本与检查

同步更新 `pyproject.toml`、`openapi-generator-config.json` 的 `packageVersion`、README 安装示例和 CHANGELOG，并运行 `uv lock`。执行 `pip install -e ".[test]"`、`ruff check .`、`mypy`、`python scripts/audit_models.py` 和 `pytest -m "not live"`；构建前运行 `python -m build --no-isolation`。

## 发布

提交并推送到 `main`，确认 CI 通过后创建并推送 `vX.Y.Z` tag。tag 会触发 GitHub Actions 校验版本、运行非 live 检查，并通过 PyPI trusted publishing 上传包和创建 GitHub Release；按需批准 `release` 环境。最后在 PyPI 确认该版本可安装。
