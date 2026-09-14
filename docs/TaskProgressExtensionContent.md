# TaskProgressExtensionContent

TaskProgressExtensionContent 的公开协议结构。 / Public contract for task progress extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | 字段 action / action field。 | 
**current_task_id** | **str** | 字段 currentTaskId / current task id field。 | [optional] 
**current_task_status** | **str** | 字段 currentTaskStatus / current task status field。 | [optional] 
**archived** | **bool** | 字段 archived / archived field。 | 
**total** | **int** | 字段 total / total field。 | 
**pending** | **int** | 字段 pending / pending field。 | 
**in_progress** | **int** | 字段 inProgress / in progress field。 | 
**completed** | **int** | 字段 completed / completed field。 | 
**progress_percent** | **int** | 字段 progressPercent / progress percent field。 | 
**tasks** | [**List[TaskSummary]**](TaskSummary.md) | 字段 tasks / tasks field。 | 

## Example

```python
from lingya_agents_sdk.models.task_progress_extension_content import TaskProgressExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of TaskProgressExtensionContent from a JSON string
task_progress_extension_content_instance = TaskProgressExtensionContent.from_json(json)
# print the JSON string representation of the object
print(TaskProgressExtensionContent.to_json())

# convert the object into a dict
task_progress_extension_content_dict = task_progress_extension_content_instance.to_dict()
# create an instance of TaskProgressExtensionContent from a dict
task_progress_extension_content_from_dict = TaskProgressExtensionContent.from_dict(task_progress_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


