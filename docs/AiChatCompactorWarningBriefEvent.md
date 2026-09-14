# AiChatCompactorWarningBriefEvent

AiChatCompactorWarningBriefEvent 的公开协议结构。 / Public contract for ai chat compactor warning brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**level** | **str** | 字段 level / level field。 | 
**warning** | **str** | 字段 warning / warning field。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_compactor_warning_brief_event import AiChatCompactorWarningBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatCompactorWarningBriefEvent from a JSON string
ai_chat_compactor_warning_brief_event_instance = AiChatCompactorWarningBriefEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatCompactorWarningBriefEvent.to_json())

# convert the object into a dict
ai_chat_compactor_warning_brief_event_dict = ai_chat_compactor_warning_brief_event_instance.to_dict()
# create an instance of AiChatCompactorWarningBriefEvent from a dict
ai_chat_compactor_warning_brief_event_from_dict = AiChatCompactorWarningBriefEvent.from_dict(ai_chat_compactor_warning_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


