# SubagentTaskSync

SubagentTaskSync 的公开协议结构。 / Public contract for subagent task sync.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_tasks** | [**List[SubagentTask]**](SubagentTask.md) | 字段 activeTasks / active tasks field。 |
**changed_tasks** | [**List[SubagentTask]**](SubagentTask.md) | 字段 changedTasks / changed tasks field。 |
**next_cursor** | **str** | 字段 nextCursor / next cursor field。 |
**polling_required** | **bool** | 字段 pollingRequired / polling required field。 |
**has_unread_terminal_results** | **bool** | 字段 hasUnreadTerminalResults / has unread terminal results field。 |

## Example

```python
from lingya_agents_sdk.models.subagent_task_sync import SubagentTaskSync

# TODO update the JSON string below
json = "{}"
# create an instance of SubagentTaskSync from a JSON string
subagent_task_sync_instance = SubagentTaskSync.from_json(json)
# print the JSON string representation of the object
print(SubagentTaskSync.to_json())

# convert the object into a dict
subagent_task_sync_dict = subagent_task_sync_instance.to_dict()
# create an instance of SubagentTaskSync from a dict
subagent_task_sync_from_dict = SubagentTaskSync.from_dict(subagent_task_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


