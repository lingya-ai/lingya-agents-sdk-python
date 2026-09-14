# AiChatRequestBriefEvent

AiChatRequestBriefEvent 的公开协议结构。 / Public contract for ai chat request brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**messages** | [**List[ChatMessage]**](ChatMessage.md) | 字段 messages / messages field。 | 
**chat_options** | [**ChatOptions**](ChatOptions.md) | 字段 chatOptions / chat options field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.ai_chat_request_brief_event import AiChatRequestBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatRequestBriefEvent from a JSON string
ai_chat_request_brief_event_instance = AiChatRequestBriefEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatRequestBriefEvent.to_json())

# convert the object into a dict
ai_chat_request_brief_event_dict = ai_chat_request_brief_event_instance.to_dict()
# create an instance of AiChatRequestBriefEvent from a dict
ai_chat_request_brief_event_from_dict = AiChatRequestBriefEvent.from_dict(ai_chat_request_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


