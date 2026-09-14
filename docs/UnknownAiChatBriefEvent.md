# UnknownAiChatBriefEvent

UnknownAiChatBriefEvent 的公开协议结构。 / Public contract for unknown ai chat brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**raw_json** | **str** | 未识别对象的原始 JSON / raw JSON for an unrecognized object。 | 

## Example

```python
from lingya_agents_sdk.models.unknown_ai_chat_brief_event import UnknownAiChatBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownAiChatBriefEvent from a JSON string
unknown_ai_chat_brief_event_instance = UnknownAiChatBriefEvent.from_json(json)
# print the JSON string representation of the object
print(UnknownAiChatBriefEvent.to_json())

# convert the object into a dict
unknown_ai_chat_brief_event_dict = unknown_ai_chat_brief_event_instance.to_dict()
# create an instance of UnknownAiChatBriefEvent from a dict
unknown_ai_chat_brief_event_from_dict = UnknownAiChatBriefEvent.from_dict(unknown_ai_chat_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


