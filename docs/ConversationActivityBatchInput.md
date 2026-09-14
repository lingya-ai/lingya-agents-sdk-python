# ConversationActivityBatchInput

ConversationActivityBatchInput 的公开协议结构。 / Public contract for conversation activity batch input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_ids** | **List[str]** | 字段 conversationIds / conversation ids field。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_activity_batch_input import ConversationActivityBatchInput

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationActivityBatchInput from a JSON string
conversation_activity_batch_input_instance = ConversationActivityBatchInput.from_json(json)
# print the JSON string representation of the object
print(ConversationActivityBatchInput.to_json())

# convert the object into a dict
conversation_activity_batch_input_dict = conversation_activity_batch_input_instance.to_dict()
# create an instance of ConversationActivityBatchInput from a dict
conversation_activity_batch_input_from_dict = ConversationActivityBatchInput.from_dict(conversation_activity_batch_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


