# AiChatStreamInput

AiChatStreamInput 的公开协议结构。 / Public contract for ai chat stream input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | 消息 ID / message ID。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_stream_input import AiChatStreamInput

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatStreamInput from a JSON string
ai_chat_stream_input_instance = AiChatStreamInput.from_json(json)
# print the JSON string representation of the object
print(AiChatStreamInput.to_json())

# convert the object into a dict
ai_chat_stream_input_dict = ai_chat_stream_input_instance.to_dict()
# create an instance of AiChatStreamInput from a dict
ai_chat_stream_input_from_dict = AiChatStreamInput.from_dict(ai_chat_stream_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


