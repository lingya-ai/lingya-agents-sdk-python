# AiChatUserQueryBriefEvent

AiChatUserQueryBriefEvent 的公开协议结构。 / Public contract for ai chat user query brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**query** | **str** | 用户问题 / user query。 | 
**attachments** | [**List[MediaAttachment]**](MediaAttachment.md) | 字段 attachments / attachments field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.ai_chat_user_query_brief_event import AiChatUserQueryBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatUserQueryBriefEvent from a JSON string
ai_chat_user_query_brief_event_instance = AiChatUserQueryBriefEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatUserQueryBriefEvent.to_json())

# convert the object into a dict
ai_chat_user_query_brief_event_dict = ai_chat_user_query_brief_event_instance.to_dict()
# create an instance of AiChatUserQueryBriefEvent from a dict
ai_chat_user_query_brief_event_from_dict = AiChatUserQueryBriefEvent.from_dict(ai_chat_user_query_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


