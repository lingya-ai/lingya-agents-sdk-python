# MediaAttachment

MediaAttachment 的公开协议结构。 / Public contract for media attachment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **int** | 文件 ID / file ID。 | 
**path** | **str** | 字段 path / path field。 | 
**file_size** | **int** | 字段 fileSize / file size field。 | 
**file_name** | **str** | 文件名 / file name。 | 
**mime_type** | **str** | MIME 类型 / MIME type。 | 

## Example

```python
from lingya_agents_sdk.models.media_attachment import MediaAttachment

# TODO update the JSON string below
json = "{}"
# create an instance of MediaAttachment from a JSON string
media_attachment_instance = MediaAttachment.from_json(json)
# print the JSON string representation of the object
print(MediaAttachment.to_json())

# convert the object into a dict
media_attachment_dict = media_attachment_instance.to_dict()
# create an instance of MediaAttachment from a dict
media_attachment_from_dict = MediaAttachment.from_dict(media_attachment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


