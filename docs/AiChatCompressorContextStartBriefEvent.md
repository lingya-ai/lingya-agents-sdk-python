# AiChatCompressorContextStartBriefEvent

AiChatCompressorContextStartBriefEvent 的公开协议结构。 / Public contract for ai chat compressor context start brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_compressor_context_start_brief_event import AiChatCompressorContextStartBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatCompressorContextStartBriefEvent from a JSON string
ai_chat_compressor_context_start_brief_event_instance = AiChatCompressorContextStartBriefEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatCompressorContextStartBriefEvent.to_json())

# convert the object into a dict
ai_chat_compressor_context_start_brief_event_dict = ai_chat_compressor_context_start_brief_event_instance.to_dict()
# create an instance of AiChatCompressorContextStartBriefEvent from a dict
ai_chat_compressor_context_start_brief_event_from_dict = AiChatCompressorContextStartBriefEvent.from_dict(ai_chat_compressor_context_start_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


