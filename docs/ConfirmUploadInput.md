# ConfirmUploadInput

ConfirmUploadInput 的公开协议结构。 / Public contract for confirm upload input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_uk** | **str** | 字段 fileUk / file uk field。 | 
**content_md5** | **str** | 字段 contentMd5 / content md5 field。 | 

## Example

```python
from lingya_agents_sdk.models.confirm_upload_input import ConfirmUploadInput

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmUploadInput from a JSON string
confirm_upload_input_instance = ConfirmUploadInput.from_json(json)
# print the JSON string representation of the object
print(ConfirmUploadInput.to_json())

# convert the object into a dict
confirm_upload_input_dict = confirm_upload_input_instance.to_dict()
# create an instance of ConfirmUploadInput from a dict
confirm_upload_input_from_dict = ConfirmUploadInput.from_dict(confirm_upload_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


