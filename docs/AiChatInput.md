# AiChatInput

AiChatInput 的公开协议结构。 / Public contract for ai chat input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | 用户问题 / user query。 |
**conversation_id** | **str** | 会话 ID / conversation ID。 | [optional]
**chat_model_spec** | [**ChatModelSpec**](ChatModelSpec.md) | 字段 chatModelSpec / chat model spec field。 | [optional]
**files** | [**List[AiChatFileRef]**](AiChatFileRef.md) | 字段 files / files field。 | [optional]
**plan_mode** | **bool** | 计划模式；省略时沿用会话设置。 / Plan mode; omitted values preserve the conversation setting. | [optional]
**goal_mode** | **bool** | 创建新目标；不能与计划模式同时开启，目标正文最多 4000 字符。 / Create a goal; cannot be enabled together with plan mode, and the objective is limited to 4000 characters. | [optional]

## Example

```python
from lingya_agents_sdk.models.ai_chat_input import AiChatInput

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatInput from a JSON string
ai_chat_input_instance = AiChatInput.from_json(json)
# print the JSON string representation of the object
print(AiChatInput.to_json())

# convert the object into a dict
ai_chat_input_dict = ai_chat_input_instance.to_dict()
# create an instance of AiChatInput from a dict
ai_chat_input_from_dict = AiChatInput.from_dict(ai_chat_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


