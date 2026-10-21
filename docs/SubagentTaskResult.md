# SubagentTaskResult

SubagentTaskResult 的公开协议结构。 / Public contract for subagent task result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task** | [**SubagentTask**](SubagentTask.md) | 字段 task / task field。 |
**result_text** | **str** | 字段 resultText / result text field。 | [optional]
**artifacts** | [**List[SubagentTaskArtifact]**](SubagentTaskArtifact.md) | 字段 artifacts / artifacts field。 |
**input_tokens** | **int** | 输入 Token 数 / input token count。 |
**output_tokens** | **int** | 输出 Token 数 / output token count。 |
**non_file_artifacts** | [**List[WorkspaceNonFileArtifact]**](WorkspaceNonFileArtifact.md) | 字段 nonFileArtifacts / non file artifacts field。 |

## Example

```python
from lingya_agents_sdk.models.subagent_task_result import SubagentTaskResult

# TODO update the JSON string below
json = "{}"
# create an instance of SubagentTaskResult from a JSON string
subagent_task_result_instance = SubagentTaskResult.from_json(json)
# print the JSON string representation of the object
print(SubagentTaskResult.to_json())

# convert the object into a dict
subagent_task_result_dict = subagent_task_result_instance.to_dict()
# create an instance of SubagentTaskResult from a dict
subagent_task_result_from_dict = SubagentTaskResult.from_dict(subagent_task_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


