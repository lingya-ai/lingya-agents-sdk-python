# FileExists

FileExists 的公开协议结构。 / Public contract for file exists.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exists** | **bool** | 字段 exists / exists field。 | 

## Example

```python
from lingya_agents_sdk.models.file_exists import FileExists

# TODO update the JSON string below
json = "{}"
# create an instance of FileExists from a JSON string
file_exists_instance = FileExists.from_json(json)
# print the JSON string representation of the object
print(FileExists.to_json())

# convert the object into a dict
file_exists_dict = file_exists_instance.to_dict()
# create an instance of FileExists from a dict
file_exists_from_dict = FileExists.from_dict(file_exists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


