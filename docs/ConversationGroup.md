# ConversationGroup

ConversationGroup 的公开协议结构。 / Public contract for conversation group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 字段 id / id field。 |
**name** | **str** | 字段 name / name field。 |
**created_time** | **datetime** | 创建时间 / creation time。 |
**last_update_time** | **datetime** | 最后更新时间 / last update time。 |

## Example

```python
from lingya_agents_sdk.models.conversation_group import ConversationGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationGroup from a JSON string
conversation_group_instance = ConversationGroup.from_json(json)
# print the JSON string representation of the object
print(ConversationGroup.to_json())

# convert the object into a dict
conversation_group_dict = conversation_group_instance.to_dict()
# create an instance of ConversationGroup from a dict
conversation_group_from_dict = ConversationGroup.from_dict(conversation_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


