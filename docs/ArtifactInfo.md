# ArtifactInfo

ArtifactInfo 的公开协议结构。 / Public contract for artifact info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **int** | 文件 ID / file ID。 | 
**file_size** | **int** | 字段 fileSize / file size field。 | 
**file_name** | **str** | 文件名 / file name。 | 
**mime_type** | **str** | MIME 类型 / MIME type。 | 
**relative_path** | **str** | 字段 relativePath / relative path field。 | [optional] 
**delivery_status** | **str** | 字段 deliveryStatus / delivery status field。 | 
**issue_codes** | **List[str]** | 字段 issueCodes / issue codes field。 | 
**recoverable** | **bool** | 字段 recoverable / recoverable field。 | 

## Example

```python
from lingya_agents_sdk.models.artifact_info import ArtifactInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArtifactInfo from a JSON string
artifact_info_instance = ArtifactInfo.from_json(json)
# print the JSON string representation of the object
print(ArtifactInfo.to_json())

# convert the object into a dict
artifact_info_dict = artifact_info_instance.to_dict()
# create an instance of ArtifactInfo from a dict
artifact_info_from_dict = ArtifactInfo.from_dict(artifact_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


