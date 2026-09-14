# AiChatErrorBriefEvent

AiChatErrorBriefEvent 的公开协议结构。 / Public contract for ai chat error brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**message** | **str** | 消息正文 / message text。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_error_brief_event import AiChatErrorBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatErrorBriefEvent from a JSON string
ai_chat_error_brief_event_instance = AiChatErrorBriefEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatErrorBriefEvent.to_json())

# convert the object into a dict
ai_chat_error_brief_event_dict = ai_chat_error_brief_event_instance.to_dict()
# create an instance of AiChatErrorBriefEvent from a dict
ai_chat_error_brief_event_from_dict = AiChatErrorBriefEvent.from_dict(ai_chat_error_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


