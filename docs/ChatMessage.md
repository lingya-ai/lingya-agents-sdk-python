# ChatMessage

ChatMessage 的公开协议结构。 / Public contract for chat message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**text** | **str** | 字段 text / text field。 | 
**metadata_raw_json** | **str** | 字段 metadataRawJson / metadata raw json field。 | [optional] 
**multimodal_attachments** | [**List[MultimodalMediaAttachment]**](MultimodalMediaAttachment.md) | 字段 multimodalAttachments / multimodal attachments field。 | [optional] 
**attachments** | [**List[MediaAttachment]**](MediaAttachment.md) | 字段 attachments / attachments field。 | [optional] 
**reasoning_text** | **str** | 字段 reasoningText / reasoning text field。 | [optional] 
**tool_calls** | [**List[ToolCall]**](ToolCall.md) | 字段 toolCalls / tool calls field。 | 
**responses** | [**List[ToolResponse]**](ToolResponse.md) | 字段 responses / responses field。 | 

## Example

```python
from lingya_agents_sdk.models.chat_message import ChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessage from a JSON string
chat_message_instance = ChatMessage.from_json(json)
# print the JSON string representation of the object
print(ChatMessage.to_json())

# convert the object into a dict
chat_message_dict = chat_message_instance.to_dict()
# create an instance of ChatMessage from a dict
chat_message_from_dict = ChatMessage.from_dict(chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


