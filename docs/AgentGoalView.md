# AgentGoalView

AgentGoalView 的公开协议结构。 / Public contract for agent goal view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal** | [**AgentGoal**](AgentGoal.md) | 字段 goal / goal field。 |

## Example

```python
from lingya_agents_sdk.models.agent_goal_view import AgentGoalView

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGoalView from a JSON string
agent_goal_view_instance = AgentGoalView.from_json(json)
# print the JSON string representation of the object
print(AgentGoalView.to_json())

# convert the object into a dict
agent_goal_view_dict = agent_goal_view_instance.to_dict()
# create an instance of AgentGoalView from a dict
agent_goal_view_from_dict = AgentGoalView.from_dict(agent_goal_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


