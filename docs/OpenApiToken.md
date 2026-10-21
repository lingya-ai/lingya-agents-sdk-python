# OpenApiToken

十分钟内有效的一次性渠道令牌，绑定签发时的渠道和用户身份。截止 expiresAt 前仅能认证一个新请求；认证成功即消费，业务失败不退还。每次新请求、重试或 SSE/WebSocket 重连都必须重新签发，不得缓存复用。使用 X-OpenAPI-Token，与所有 HMAC 鉴权头互斥，不能用于 presign。 / A single-use channel token valid for ten minutes, bound to the issuing channel and user. It authenticates only one new request before expiresAt and is consumed on successful authentication even if the business operation fails. Obtain a fresh token for every new request, retry, or SSE/WebSocket reconnection; never cache or reuse it. Send X-OpenAPI-Token without any HMAC authentication headers; tokens cannot call presign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** | 一次性令牌原文，不得写入日志。 / Single-use token; never log its value. |
**expires_at** | **datetime** | 未消费令牌的截止时间，不代表截止前可以重复使用。 / Deadline for an unused token, not a reusable session lifetime. |

## Example

```python
from lingya_agents_sdk.models.open_api_token import OpenApiToken

# TODO update the JSON string below
json = "{}"
# create an instance of OpenApiToken from a JSON string
open_api_token_instance = OpenApiToken.from_json(json)
# print the JSON string representation of the object
print(OpenApiToken.to_json())

# convert the object into a dict
open_api_token_dict = open_api_token_instance.to_dict()
# create an instance of OpenApiToken from a dict
open_api_token_from_dict = OpenApiToken.from_dict(open_api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


