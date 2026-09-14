# ModelKeyGroup

ModelKeyGroup 的公开协议结构。 / Public contract for model key group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_group_id** | **int** | 字段 keyGroupId / key group id field。 | 
**key_group_name** | **str** | 字段 keyGroupName / key group name field。 | 
**models** | [**List[ChatModelConfig]**](ChatModelConfig.md) | 字段 models / models field。 | 

## Example

```python
from lingya_agents_sdk.models.model_key_group import ModelKeyGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ModelKeyGroup from a JSON string
model_key_group_instance = ModelKeyGroup.from_json(json)
# print the JSON string representation of the object
print(ModelKeyGroup.to_json())

# convert the object into a dict
model_key_group_dict = model_key_group_instance.to_dict()
# create an instance of ModelKeyGroup from a dict
model_key_group_from_dict = ModelKeyGroup.from_dict(model_key_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


