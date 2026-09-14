# AssistantChatMessage

AssistantChatMessage 的公开协议结构。 / Public contract for assistant chat message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**text** | **str** | 字段 text / text field。 | [optional] 
**reasoning_text** | **str** | 字段 reasoningText / reasoning text field。 | [optional] 
**tool_calls** | [**List[ToolCall]**](ToolCall.md) | 字段 toolCalls / tool calls field。 | 
**metadata_raw_json** | **str** | 字段 metadataRawJson / metadata raw json field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.assistant_chat_message import AssistantChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of AssistantChatMessage from a JSON string
assistant_chat_message_instance = AssistantChatMessage.from_json(json)
# print the JSON string representation of the object
print(AssistantChatMessage.to_json())

# convert the object into a dict
assistant_chat_message_dict = assistant_chat_message_instance.to_dict()
# create an instance of AssistantChatMessage from a dict
assistant_chat_message_from_dict = AssistantChatMessage.from_dict(assistant_chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


