# AiChatInput

AiChatInput 的公开协议结构。 / Public contract for ai chat input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** | 用户问题 / user query。 | 
**conversation_id** | **str** | 会话 ID / conversation ID。 | [optional] 
**chat_model_spec** | [**ChatModelSpec**](ChatModelSpec.md) | 字段 chatModelSpec / chat model spec field。 | [optional] 
**files** | [**List[AiChatFileRef]**](AiChatFileRef.md) | 字段 files / files field。 | [optional] 

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


