# ValidationError

ValidationError 的公开协议结构。 / Public contract for validation error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 字段 code / code field。 | 
**message** | **str** | 消息正文 / message text。 | 
**fields** | [**List[FieldError]**](FieldError.md) | 字段 fields / fields field。 | 

## Example

```python
from lingya_agents_sdk.models.validation_error import ValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of ValidationError from a JSON string
validation_error_instance = ValidationError.from_json(json)
# print the JSON string representation of the object
print(ValidationError.to_json())

# convert the object into a dict
validation_error_dict = validation_error_instance.to_dict()
# create an instance of ValidationError from a dict
validation_error_from_dict = ValidationError.from_dict(validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


