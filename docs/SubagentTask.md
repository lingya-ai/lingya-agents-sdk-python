# SubagentTask

SubagentTask 的公开协议结构。 / Public contract for subagent task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | 异步任务 ID / asynchronous task ID。 |
**description** | **str** | 可读说明 / human-readable description。 |
**subagent_type** | **str** | 字段 subagentType / subagent type field。 |
**status** | **str** | 当前状态 / current status。 |
**phase** | **str** | 字段 phase / phase field。 | [optional]
**parent_conversation_id** | **str** | 字段 parentConversationId / parent conversation id field。 |
**parent_message_id** | **str** | 字段 parentMessageId / parent message id field。 |
**child_conversation_id** | **str** | 字段 childConversationId / child conversation id field。 | [optional]
**child_message_id** | **str** | 字段 childMessageId / child message id field。 | [optional]
**result_available** | **bool** | 字段 resultAvailable / result available field。 |
**artifact_count** | **int** | 字段 artifactCount / artifact count field。 |
**notification_status** | **str** | 字段 notificationStatus / notification status field。 |
**failure_code** | **str** | 字段 failureCode / failure code field。 | [optional]
**failure_message** | **str** | 字段 failureMessage / failure message field。 | [optional]
**created_time** | **datetime** | 创建时间 / creation time。 |
**started_time** | **datetime** | 字段 startedTime / started time field。 | [optional]
**completed_time** | **datetime** | 字段 completedTime / completed time field。 | [optional]
**last_update_time** | **datetime** | 最后更新时间 / last update time。 |
**cancellable** | **bool** | 字段 cancellable / cancellable field。 |

## Example

```python
from lingya_agents_sdk.models.subagent_task import SubagentTask

# TODO update the JSON string below
json = "{}"
# create an instance of SubagentTask from a JSON string
subagent_task_instance = SubagentTask.from_json(json)
# print the JSON string representation of the object
print(SubagentTask.to_json())

# convert the object into a dict
subagent_task_dict = subagent_task_instance.to_dict()
# create an instance of SubagentTask from a dict
subagent_task_from_dict = SubagentTask.from_dict(subagent_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


