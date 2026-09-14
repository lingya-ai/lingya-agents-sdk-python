# WorkspaceNonFileArtifact

WorkspaceNonFileArtifact 的公开协议结构。 / Public contract for workspace non file artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_id** | **str** | 字段 artifactId / artifact id field。 | 
**kind** | **str** | 字段 kind / kind field。 | 
**title** | **str** | 标题 / title。 | 
**description** | **str** | 可读说明 / human-readable description。 | [optional] 
**last_update_time** | **datetime** | 最后更新时间 / last update time。 | 
**preview_url** | **str** | 字段 previewUrl / preview url field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.workspace_non_file_artifact import WorkspaceNonFileArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceNonFileArtifact from a JSON string
workspace_non_file_artifact_instance = WorkspaceNonFileArtifact.from_json(json)
# print the JSON string representation of the object
print(WorkspaceNonFileArtifact.to_json())

# convert the object into a dict
workspace_non_file_artifact_dict = workspace_non_file_artifact_instance.to_dict()
# create an instance of WorkspaceNonFileArtifact from a dict
workspace_non_file_artifact_from_dict = WorkspaceNonFileArtifact.from_dict(workspace_non_file_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


