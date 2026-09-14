# DefaultModel

DefaultModel 的公开协议结构。 / Public contract for default model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_group_id** | **int** | 字段 keyGroupId / key group id field。 | 
**model** | **str** | 字段 model / model field。 | 

## Example

```python
from lingya_agents_sdk.models.default_model import DefaultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultModel from a JSON string
default_model_instance = DefaultModel.from_json(json)
# print the JSON string representation of the object
print(DefaultModel.to_json())

# convert the object into a dict
default_model_dict = default_model_instance.to_dict()
# create an instance of DefaultModel from a dict
default_model_from_dict = DefaultModel.from_dict(default_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


