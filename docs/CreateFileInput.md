# CreateFileInput

CreateFileInput 的公开协议结构。 / Public contract for create file input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | 文件名 / file name。 | 
**content_md5** | **str** | 字段 contentMd5 / content md5 field。 | 

## Example

```python
from lingya_agents_sdk.models.create_file_input import CreateFileInput

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFileInput from a JSON string
create_file_input_instance = CreateFileInput.from_json(json)
# print the JSON string representation of the object
print(CreateFileInput.to_json())

# convert the object into a dict
create_file_input_dict = create_file_input_instance.to_dict()
# create an instance of CreateFileInput from a dict
create_file_input_from_dict = CreateFileInput.from_dict(create_file_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


