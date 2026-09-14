# ReturnedReference

ReturnedReference 的公开协议结构。 / Public contract for returned reference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**reference_id** | **int** | 字段 referenceId / reference id field。 | 

## Example

```python
from lingya_agents_sdk.models.returned_reference import ReturnedReference

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnedReference from a JSON string
returned_reference_instance = ReturnedReference.from_json(json)
# print the JSON string representation of the object
print(ReturnedReference.to_json())

# convert the object into a dict
returned_reference_dict = returned_reference_instance.to_dict()
# create an instance of ReturnedReference from a dict
returned_reference_from_dict = ReturnedReference.from_dict(returned_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


