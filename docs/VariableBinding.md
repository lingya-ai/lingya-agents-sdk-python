# VariableBinding

VariableBinding 的公开协议结构。 / Public contract for variable binding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 | 
**value** | **str** | 字段 value / value field。 | 

## Example

```python
from lingya_agents_sdk.models.variable_binding import VariableBinding

# TODO update the JSON string below
json = "{}"
# create an instance of VariableBinding from a JSON string
variable_binding_instance = VariableBinding.from_json(json)
# print the JSON string representation of the object
print(VariableBinding.to_json())

# convert the object into a dict
variable_binding_dict = variable_binding_instance.to_dict()
# create an instance of VariableBinding from a dict
variable_binding_from_dict = VariableBinding.from_dict(variable_binding_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


