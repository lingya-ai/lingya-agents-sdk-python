# AgentAsyncTaskSync

AgentAsyncTaskSync 的公开协议结构。 / Public contract for agent async task sync.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_tasks** | [**List[AsyncTask]**](AsyncTask.md) | 字段 activeTasks / active tasks field。 |
**notification_messages** | [**List[ConversationMessage]**](ConversationMessage.md) | 字段 notificationMessages / notification messages field。 |
**next_message_id** | **str** | 字段 nextMessageId / next message id field。 |
**has_more** | **bool** | 字段 hasMore / has more field。 |
**polling_required** | **bool** | 字段 pollingRequired / polling required field。 |

## Example

```python
from lingya_agents_sdk.models.agent_async_task_sync import AgentAsyncTaskSync

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAsyncTaskSync from a JSON string
agent_async_task_sync_instance = AgentAsyncTaskSync.from_json(json)
# print the JSON string representation of the object
print(AgentAsyncTaskSync.to_json())

# convert the object into a dict
agent_async_task_sync_dict = agent_async_task_sync_instance.to_dict()
# create an instance of AgentAsyncTaskSync from a dict
agent_async_task_sync_from_dict = AgentAsyncTaskSync.from_dict(agent_async_task_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


