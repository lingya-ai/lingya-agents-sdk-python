# MultimodalMediaAttachment

MultimodalMediaAttachment 的公开协议结构。 / Public contract for multimodal media attachment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | 文件名 / file name。 | 
**mime_type** | **str** | MIME 类型 / MIME type。 | 
**data** | **str** | 字段 data / data field。 | 

## Example

```python
from lingya_agents_sdk.models.multimodal_media_attachment import MultimodalMediaAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of MultimodalMediaAttachment from a JSON string
multimodal_media_attachment_instance = MultimodalMediaAttachment.from_json(json)
# print the JSON string representation of the object
print(MultimodalMediaAttachment.to_json())

# convert the object into a dict
multimodal_media_attachment_dict = multimodal_media_attachment_instance.to_dict()
# create an instance of MultimodalMediaAttachment from a dict
multimodal_media_attachment_from_dict = MultimodalMediaAttachment.from_dict(multimodal_media_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


