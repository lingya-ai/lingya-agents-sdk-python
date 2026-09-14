# AttachmentExtension

AttachmentExtension 的公开协议结构。 / Public contract for attachment extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ext** | **str** | 字段 ext / ext field。 | 
**media** | **str** | 字段 media / media field。 | 

## Example

```python
from lingya_agents_sdk.models.attachment_extension import AttachmentExtension

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentExtension from a JSON string
attachment_extension_instance = AttachmentExtension.from_json(json)
# print the JSON string representation of the object
print(AttachmentExtension.to_json())

# convert the object into a dict
attachment_extension_dict = attachment_extension_instance.to_dict()
# create an instance of AttachmentExtension from a dict
attachment_extension_from_dict = AttachmentExtension.from_dict(attachment_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


