# WorkspaceArtifactList

WorkspaceArtifactList 的公开协议结构。 / Public contract for workspace artifact list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_artifacts** | [**WorkspaceFilePage**](WorkspaceFilePage.md) | 字段 fileArtifacts / file artifacts field。 | 
**non_file_artifacts** | [**List[WorkspaceNonFileArtifact]**](WorkspaceNonFileArtifact.md) | 字段 nonFileArtifacts / non file artifacts field。 | 

## Example

```python
from lingya_agents_sdk.models.workspace_artifact_list import WorkspaceArtifactList

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceArtifactList from a JSON string
workspace_artifact_list_instance = WorkspaceArtifactList.from_json(json)
# print the JSON string representation of the object
print(WorkspaceArtifactList.to_json())

# convert the object into a dict
workspace_artifact_list_dict = workspace_artifact_list_instance.to_dict()
# create an instance of WorkspaceArtifactList from a dict
workspace_artifact_list_from_dict = WorkspaceArtifactList.from_dict(workspace_artifact_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


