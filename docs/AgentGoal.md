# AgentGoal

AgentGoal 的公开协议结构。 / Public contract for agent goal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal_id** | **str** | 字段 goalId / goal id field。 |
**goal_revision** | **int** | 字段 goalRevision / goal revision field。 |
**objective** | **str** | 字段 objective / objective field。 |
**phase** | **str** | 字段 phase / phase field。 |
**record_state** | **str** | 字段 recordState / record state field。 |
**activation_state** | **str** | 字段 activationState / activation state field。 |
**effectively_armed** | **bool** | 字段 effectivelyArmed / effectively armed field。 |
**blocked_code** | **str** | 字段 blockedCode / blocked code field。 |
**blocked_message** | **str** | 字段 blockedMessage / blocked message field。 |
**completion_message** | **str** | 字段 completionMessage / completion message field。 |
**status_version** | **int** | 字段 statusVersion / status version field。 |
**next_execution_due_time** | **datetime** | 字段 nextExecutionDueTime / next execution due time field。 |

## Example

```python
from lingya_agents_sdk.models.agent_goal import AgentGoal

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGoal from a JSON string
agent_goal_instance = AgentGoal.from_json(json)
# print the JSON string representation of the object
print(AgentGoal.to_json())

# convert the object into a dict
agent_goal_dict = agent_goal_instance.to_dict()
# create an instance of AgentGoal from a dict
agent_goal_from_dict = AgentGoal.from_dict(agent_goal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


