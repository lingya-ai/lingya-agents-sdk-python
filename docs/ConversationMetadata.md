# ConversationMetadata

ConversationMetadata 的公开协议结构。 / Public contract for conversation metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | 会话 ID / conversation ID。 |
**status** | **str** | 当前状态 / current status。 |
**title** | **str** | 标题 / title。 |
**title_state** | **str** | 字段 titleState / title state field。 |
**group_id** | **int** | 字段 groupId / group id field。 |
**group_name** | **str** | 字段 groupName / group name field。 |
**last_update_time** | **datetime** | 最后更新时间 / last update time。 |

## Example

```python
from lingya_agents_sdk.models.conversation_metadata import ConversationMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMetadata from a JSON string
conversation_metadata_instance = ConversationMetadata.from_json(json)
# print the JSON string representation of the object
print(ConversationMetadata.to_json())

# convert the object into a dict
conversation_metadata_dict = conversation_metadata_instance.to_dict()
# create an instance of ConversationMetadata from a dict
conversation_metadata_from_dict = ConversationMetadata.from_dict(conversation_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


