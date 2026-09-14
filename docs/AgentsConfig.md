# AgentsConfig

AgentsConfig 的公开协议结构。 / Public contract for agents config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_model_config** | [**ModelConfig**](ModelConfig.md) | 字段 modelConfig / model config field。 | 
**support_attachment_ext** | [**List[AttachmentExtension]**](AttachmentExtension.md) | 字段 supportAttachmentExt / support attachment ext field。 | 
**max_attachment_count** | **int** | 字段 maxAttachmentCount / max attachment count field。 | 

## Example

```python
from lingya_agents_sdk.models.agents_config import AgentsConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AgentsConfig from a JSON string
agents_config_instance = AgentsConfig.from_json(json)
# print the JSON string representation of the object
print(AgentsConfig.to_json())

# convert the object into a dict
agents_config_dict = agents_config_instance.to_dict()
# create an instance of AgentsConfig from a dict
agents_config_from_dict = AgentsConfig.from_dict(agents_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


