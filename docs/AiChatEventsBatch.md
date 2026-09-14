# AiChatEventsBatch

AiChatEventsBatch 的公开协议结构。 / Public contract for ai chat events batch.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[AiChatMessageEvent]**](AiChatMessageEvent.md) | 记录列表 / records。 | 
**skipped** | [**List[AiChatEventsBatchSkipped]**](AiChatEventsBatchSkipped.md) | 字段 skipped / skipped field。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_events_batch import AiChatEventsBatch

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatEventsBatch from a JSON string
ai_chat_events_batch_instance = AiChatEventsBatch.from_json(json)
# print the JSON string representation of the object
print(AiChatEventsBatch.to_json())

# convert the object into a dict
ai_chat_events_batch_dict = ai_chat_events_batch_instance.to_dict()
# create an instance of AiChatEventsBatch from a dict
ai_chat_events_batch_from_dict = AiChatEventsBatch.from_dict(ai_chat_events_batch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


