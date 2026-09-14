# AiChatEventsBatchSkipped

AiChatEventsBatchSkipped 的公开协议结构。 / Public contract for ai chat events batch skipped.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | 消息 ID / message ID。 | 
**reason** | **str** | 字段 reason / reason field。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_events_batch_skipped import AiChatEventsBatchSkipped

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatEventsBatchSkipped from a JSON string
ai_chat_events_batch_skipped_instance = AiChatEventsBatchSkipped.from_json(json)
# print the JSON string representation of the object
print(AiChatEventsBatchSkipped.to_json())

# convert the object into a dict
ai_chat_events_batch_skipped_dict = ai_chat_events_batch_skipped_instance.to_dict()
# create an instance of AiChatEventsBatchSkipped from a dict
ai_chat_events_batch_skipped_from_dict = AiChatEventsBatchSkipped.from_dict(ai_chat_events_batch_skipped_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


