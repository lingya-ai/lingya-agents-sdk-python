# GeneratePreSignedUrlInput

GeneratePreSignedUrlInput 的公开协议结构。 / Public contract for generate pre signed url input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | 文件名 / file name。 | 
**module** | **str** | 字段 module / module field。 | 
**content_md5** | **str** | 字段 contentMd5 / content md5 field。 | 
**file_id** | **int** | 文件 ID / file ID。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.generate_pre_signed_url_input import GeneratePreSignedUrlInput

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratePreSignedUrlInput from a JSON string
generate_pre_signed_url_input_instance = GeneratePreSignedUrlInput.from_json(json)
# print the JSON string representation of the object
print(GeneratePreSignedUrlInput.to_json())

# convert the object into a dict
generate_pre_signed_url_input_dict = generate_pre_signed_url_input_instance.to_dict()
# create an instance of GeneratePreSignedUrlInput from a dict
generate_pre_signed_url_input_from_dict = GeneratePreSignedUrlInput.from_dict(generate_pre_signed_url_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


