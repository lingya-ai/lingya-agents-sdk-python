# EditAgentGoalInput

EditAgentGoalInput 的公开协议结构。 / Public contract for edit agent goal input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**goal_id** | **str** | 字段 goalId / goal id field。 |
**goal_revision** | **int** | 字段 goalRevision / goal revision field。 |
**objective** | **str** | 字段 objective / objective field。 |

## Example

```python
from lingya_agents_sdk.models.edit_agent_goal_input import EditAgentGoalInput

# TODO update the JSON string below
json = "{}"
# create an instance of EditAgentGoalInput from a JSON string
edit_agent_goal_input_instance = EditAgentGoalInput.from_json(json)
# print the JSON string representation of the object
print(EditAgentGoalInput.to_json())

# convert the object into a dict
edit_agent_goal_input_dict = edit_agent_goal_input_instance.to_dict()
# create an instance of EditAgentGoalInput from a dict
edit_agent_goal_input_from_dict = EditAgentGoalInput.from_dict(edit_agent_goal_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


