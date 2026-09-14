# WorkspaceFilePage

WorkspaceFilePage 的公开协议结构。 / Public contract for workspace file page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[WorkspaceFile]**](WorkspaceFile.md) | 记录列表 / records。 | 
**page** | [**PageInfo**](PageInfo.md) | 分页信息 / page metadata。 | 

## Example

```python
from lingya_agents_sdk.models.workspace_file_page import WorkspaceFilePage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceFilePage from a JSON string
workspace_file_page_instance = WorkspaceFilePage.from_json(json)
# print the JSON string representation of the object
print(WorkspaceFilePage.to_json())

# convert the object into a dict
workspace_file_page_dict = workspace_file_page_instance.to_dict()
# create an instance of WorkspaceFilePage from a dict
workspace_file_page_from_dict = WorkspaceFilePage.from_dict(workspace_file_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


