# ConversationGroupList

ConversationGroupList 的公开协议结构。 / Public contract for conversation group list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[ConversationGroup]**](ConversationGroup.md) | 记录列表 / records。 |

## Example

```python
from lingya_agents_sdk.models.conversation_group_list import ConversationGroupList

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationGroupList from a JSON string
conversation_group_list_instance = ConversationGroupList.from_json(json)
# print the JSON string representation of the object
print(ConversationGroupList.to_json())

# convert the object into a dict
conversation_group_list_dict = conversation_group_list_instance.to_dict()
# create an instance of ConversationGroupList from a dict
conversation_group_list_from_dict = ConversationGroupList.from_dict(conversation_group_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


