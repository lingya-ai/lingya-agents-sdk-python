# ConversationGroupDeleted

ConversationGroupDeleted 的公开协议结构。 / Public contract for conversation group deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | 字段 groupId / group id field。 |
**moved_conversation_count** | **int** | 字段 movedConversationCount / moved conversation count field。 |

## Example

```python
from lingya_agents_sdk.models.conversation_group_deleted import ConversationGroupDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationGroupDeleted from a JSON string
conversation_group_deleted_instance = ConversationGroupDeleted.from_json(json)
# print the JSON string representation of the object
print(ConversationGroupDeleted.to_json())

# convert the object into a dict
conversation_group_deleted_dict = conversation_group_deleted_instance.to_dict()
# create an instance of ConversationGroupDeleted from a dict
conversation_group_deleted_from_dict = ConversationGroupDeleted.from_dict(conversation_group_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


