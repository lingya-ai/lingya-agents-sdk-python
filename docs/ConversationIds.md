# ConversationIds

ConversationIds 的公开协议结构。 / Public contract for conversation ids.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_ids** | **List[str]** | 字段 conversationIds / conversation ids field。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_ids import ConversationIds

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationIds from a JSON string
conversation_ids_instance = ConversationIds.from_json(json)
# print the JSON string representation of the object
print(ConversationIds.to_json())

# convert the object into a dict
conversation_ids_dict = conversation_ids_instance.to_dict()
# create an instance of ConversationIds from a dict
conversation_ids_from_dict = ConversationIds.from_dict(conversation_ids_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


