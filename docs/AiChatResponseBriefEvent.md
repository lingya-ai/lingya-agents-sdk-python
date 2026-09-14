# AiChatResponseBriefEvent

AiChatResponseBriefEvent 的公开协议结构。 / Public contract for ai chat response brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**assistant_messages** | [**List[AssistantChatMessage]**](AssistantChatMessage.md) | 字段 assistantMessages / assistant messages field。 | 
**usage** | [**Usage**](Usage.md) | 字段 usage / usage field。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_response_brief_event import AiChatResponseBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatResponseBriefEvent from a JSON string
ai_chat_response_brief_event_instance = AiChatResponseBriefEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatResponseBriefEvent.to_json())

# convert the object into a dict
ai_chat_response_brief_event_dict = ai_chat_response_brief_event_instance.to_dict()
# create an instance of AiChatResponseBriefEvent from a dict
ai_chat_response_brief_event_from_dict = AiChatResponseBriefEvent.from_dict(ai_chat_response_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


