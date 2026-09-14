# ConversationUserMessage

ConversationUserMessage 的公开协议结构。 / Public contract for conversation user message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | 字段 text / text field。 | 
**multimodal_attachments** | [**List[MultimodalMediaAttachment]**](MultimodalMediaAttachment.md) | 字段 multimodalAttachments / multimodal attachments field。 | [optional] 
**attachments** | [**List[MediaAttachment]**](MediaAttachment.md) | 字段 attachments / attachments field。 | [optional] 
**metadata_raw_json** | **str** | 字段 metadataRawJson / metadata raw json field。 | [optional] 
**execution_type** | **str** | 字段 executionType / execution type field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_user_message import ConversationUserMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationUserMessage from a JSON string
conversation_user_message_instance = ConversationUserMessage.from_json(json)
# print the JSON string representation of the object
print(ConversationUserMessage.to_json())

# convert the object into a dict
conversation_user_message_dict = conversation_user_message_instance.to_dict()
# create an instance of ConversationUserMessage from a dict
conversation_user_message_from_dict = ConversationUserMessage.from_dict(conversation_user_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


