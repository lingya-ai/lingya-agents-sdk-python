# AgentGoalConfig

AgentGoalConfig 的公开协议结构。 / Public contract for agent goal config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported** | **bool** | 字段 supported / supported field。 |
**continuation_enabled** | **bool** | 字段 continuationEnabled / continuation enabled field。 |

## Example

```python
from lingya_agents_sdk.models.agent_goal_config import AgentGoalConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AgentGoalConfig from a JSON string
agent_goal_config_instance = AgentGoalConfig.from_json(json)
# print the JSON string representation of the object
print(AgentGoalConfig.to_json())

# convert the object into a dict
agent_goal_config_dict = agent_goal_config_instance.to_dict()
# create an instance of AgentGoalConfig from a dict
agent_goal_config_from_dict = AgentGoalConfig.from_dict(agent_goal_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


