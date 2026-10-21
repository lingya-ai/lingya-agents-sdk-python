# AgentGoalRefInput

AgentGoalRefInput 的公开协议结构。 / Public contract for agent goal ref input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal_id** | **str** | 字段 goalId / goal id field。 |
**goal_revision** | **int** | 字段 goalRevision / goal revision field。 |

## Example

```python
from lingya_agents_sdk.models.agent_goal_ref_input import AgentGoalRefInput

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGoalRefInput from a JSON string
agent_goal_ref_input_instance = AgentGoalRefInput.from_json(json)
# print the JSON string representation of the object
print(AgentGoalRefInput.to_json())

# convert the object into a dict
agent_goal_ref_input_dict = agent_goal_ref_input_instance.to_dict()
# create an instance of AgentGoalRefInput from a dict
agent_goal_ref_input_from_dict = AgentGoalRefInput.from_dict(agent_goal_ref_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


