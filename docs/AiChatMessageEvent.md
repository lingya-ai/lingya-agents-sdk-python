# AiChatMessageEvent

AiChatMessageEvent 的公开协议结构。 / Public contract for ai chat message event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | 消息 ID / message ID。 | 
**events** | [**List[AiChatBriefEvent]**](AiChatBriefEvent.md) | 字段 events / events field。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_message_event import AiChatMessageEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatMessageEvent from a JSON string
ai_chat_message_event_instance = AiChatMessageEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatMessageEvent.to_json())

# convert the object into a dict
ai_chat_message_event_dict = ai_chat_message_event_instance.to_dict()
# create an instance of AiChatMessageEvent from a dict
ai_chat_message_event_from_dict = AiChatMessageEvent.from_dict(ai_chat_message_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


