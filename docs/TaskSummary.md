# TaskSummary

TaskSummary 的公开协议结构。 / Public contract for task summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 字段 id / id field。 |
**content** | **str** | 任务内容 / task content。 |
**status** | **str** | 当前状态 / current status。 |

## Example

```python
from lingya_agents_sdk.models.task_summary import TaskSummary

# TODO update the JSON string below
json = "{}"
# create an instance of TaskSummary from a JSON string
task_summary_instance = TaskSummary.from_json(json)
# print the JSON string representation of the object
print(TaskSummary.to_json())

# convert the object into a dict
task_summary_dict = task_summary_instance.to_dict()
# create an instance of TaskSummary from a dict
task_summary_from_dict = TaskSummary.from_dict(task_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


