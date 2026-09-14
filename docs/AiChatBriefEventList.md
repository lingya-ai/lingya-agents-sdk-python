# AiChatBriefEventList

AiChatBriefEventList 的公开协议结构。 / Public contract for ai chat brief event list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[AiChatBriefEvent]**](AiChatBriefEvent.md) | 记录列表 / records。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_brief_event_list import AiChatBriefEventList

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatBriefEventList from a JSON string
ai_chat_brief_event_list_instance = AiChatBriefEventList.from_json(json)
# print the JSON string representation of the object
print(AiChatBriefEventList.to_json())

# convert the object into a dict
ai_chat_brief_event_list_dict = ai_chat_brief_event_list_instance.to_dict()
# create an instance of AiChatBriefEventList from a dict
ai_chat_brief_event_list_from_dict = AiChatBriefEventList.from_dict(ai_chat_brief_event_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


