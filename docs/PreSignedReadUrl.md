# PreSignedReadUrl

PreSignedReadUrl 的公开协议结构。 / Public contract for pre signed read url.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | 预签名 URL / presigned URL。 | 

## Example

```python
from lingya_agents_sdk.models.pre_signed_read_url import PreSignedReadUrl

# TODO update the JSON string below
json = "{}"
# create an instance of PreSignedReadUrl from a JSON string
pre_signed_read_url_instance = PreSignedReadUrl.from_json(json)
# print the JSON string representation of the object
print(PreSignedReadUrl.to_json())

# convert the object into a dict
pre_signed_read_url_dict = pre_signed_read_url_instance.to_dict()
# create an instance of PreSignedReadUrl from a dict
pre_signed_read_url_from_dict = PreSignedReadUrl.from_dict(pre_signed_read_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


