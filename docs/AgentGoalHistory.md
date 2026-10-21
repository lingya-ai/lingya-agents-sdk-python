# AgentGoalHistory

AgentGoalHistory 的公开协议结构。 / Public contract for agent goal history.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[AgentGoal]**](AgentGoal.md) | 字段 items / items field。 |
**page** | **int** | 分页信息 / page metadata。 |
**size** | **int** | 大小（字节）或分页容量 / byte size or page size。 |
**has_next** | **bool** | 字段 hasNext / has next field。 |

## Example

```python
from lingya_agents_sdk.models.agent_goal_history import AgentGoalHistory

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGoalHistory from a JSON string
agent_goal_history_instance = AgentGoalHistory.from_json(json)
# print the JSON string representation of the object
print(AgentGoalHistory.to_json())

# convert the object into a dict
agent_goal_history_dict = agent_goal_history_instance.to_dict()
# create an instance of AgentGoalHistory from a dict
agent_goal_history_from_dict = AgentGoalHistory.from_dict(agent_goal_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


