# GeneratePreSignedUrlOutput

GeneratePreSignedUrlOutput 的公开协议结构。 / Public contract for generate pre signed url output.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**support** | **bool** | 当前存储是否支持该操作 / whether the storage supports this operation。 | 
**file_uk** | **str** | 字段 fileUk / file uk field。 | [optional] 
**url** | **str** | 预签名 URL / presigned URL。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.generate_pre_signed_url_output import GeneratePreSignedUrlOutput

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratePreSignedUrlOutput from a JSON string
generate_pre_signed_url_output_instance = GeneratePreSignedUrlOutput.from_json(json)
# print the JSON string representation of the object
print(GeneratePreSignedUrlOutput.to_json())

# convert the object into a dict
generate_pre_signed_url_output_dict = generate_pre_signed_url_output_instance.to_dict()
# create an instance of GeneratePreSignedUrlOutput from a dict
generate_pre_signed_url_output_from_dict = GeneratePreSignedUrlOutput.from_dict(generate_pre_signed_url_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


