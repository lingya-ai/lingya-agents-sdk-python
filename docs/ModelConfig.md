# ModelConfig

ModelConfig 的公开协议结构。 / Public contract for model config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_model** | [**DefaultModel**](DefaultModel.md) | 字段 defaultModel / default model field。 | 
**model_key_groups** | [**List[ModelKeyGroup]**](ModelKeyGroup.md) | 字段 modelKeyGroups / model key groups field。 | 

## Example

```python
from lingya_agents_sdk.models.model_config import ModelConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ModelConfig from a JSON string
model_config_instance = ModelConfig.from_json(json)
# print the JSON string representation of the object
print(ModelConfig.to_json())

# convert the object into a dict
model_config_dict = model_config_instance.to_dict()
# create an instance of ModelConfig from a dict
model_config_from_dict = ModelConfig.from_dict(model_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


