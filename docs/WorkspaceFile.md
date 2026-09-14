# WorkspaceFile

WorkspaceFile 的公开协议结构。 / Public contract for workspace file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relative_path** | **str** | 字段 relativePath / relative path field。 | 
**size** | **int** | 大小（字节）或分页容量 / byte size or page size。 | 
**file_name** | **str** | 文件名 / file name。 | 
**mime_type** | **str** | MIME 类型 / MIME type。 | 
**last_update_time** | **datetime** | 最后更新时间 / last update time。 | 

## Example

```python
from lingya_agents_sdk.models.workspace_file import WorkspaceFile

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceFile from a JSON string
workspace_file_instance = WorkspaceFile.from_json(json)
# print the JSON string representation of the object
print(WorkspaceFile.to_json())

# convert the object into a dict
workspace_file_dict = workspace_file_instance.to_dict()
# create an instance of WorkspaceFile from a dict
workspace_file_from_dict = WorkspaceFile.from_dict(workspace_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


