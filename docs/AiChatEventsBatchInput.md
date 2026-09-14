# AiChatEventsBatchInput

AiChatEventsBatchInput 的公开协议结构。 / Public contract for ai chat events batch input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | 会话 ID / conversation ID。 | 
**message_ids** | **List[str]** | 字段 messageIds / message ids field。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_events_batch_input import AiChatEventsBatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatEventsBatchInput from a JSON string
ai_chat_events_batch_input_instance = AiChatEventsBatchInput.from_json(json)
# print the JSON string representation of the object
print(AiChatEventsBatchInput.to_json())

# convert the object into a dict
ai_chat_events_batch_input_dict = ai_chat_events_batch_input_instance.to_dict()
# create an instance of AiChatEventsBatchInput from a dict
ai_chat_events_batch_input_from_dict = AiChatEventsBatchInput.from_dict(ai_chat_events_batch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


