# SubagentTaskArtifact

SubagentTaskArtifact 的公开协议结构。 / Public contract for subagent task artifact.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**artifact_id** | **str** | 字段 artifactId / artifact id field。 |
**name** | **str** | 字段 name / name field。 |
**mime_type** | **str** | MIME 类型 / MIME type。 | [optional]
**size** | **int** | 大小（字节）或分页容量 / byte size or page size。 | [optional]
**relative_path** | **str** | 字段 relativePath / relative path field。 | [optional]
**delivery_status** | **str** | 字段 deliveryStatus / delivery status field。 |
**issue_codes** | **List[str]** | 字段 issueCodes / issue codes field。 |
**recoverable** | **bool** | 字段 recoverable / recoverable field。 |

## Example

```python
from lingya_agents_sdk.models.subagent_task_artifact import SubagentTaskArtifact

# TODO update the JSON string below
json = "{}"
# create an instance of SubagentTaskArtifact from a JSON string
subagent_task_artifact_instance = SubagentTaskArtifact.from_json(json)
# print the JSON string representation of the object
print(SubagentTaskArtifact.to_json())

# convert the object into a dict
subagent_task_artifact_dict = subagent_task_artifact_instance.to_dict()
# create an instance of SubagentTaskArtifact from a dict
subagent_task_artifact_from_dict = SubagentTaskArtifact.from_dict(subagent_task_artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


