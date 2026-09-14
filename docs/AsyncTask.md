# AsyncTask

AsyncTask 的公开协议结构。 / Public contract for async task.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**task_id** | **str** | 异步任务 ID / asynchronous task ID。 | 
**task_type** | **str** | 字段 taskType / task type field。 | 
**title** | **str** | 标题 / title。 | 
**status** | **str** | 当前状态 / current status。 | 
**progress_percent** | **int** | 字段 progressPercent / progress percent field。 | [optional] 
**phase** | **str** | 字段 phase / phase field。 | [optional] 
**status_message** | **str** | 字段 statusMessage / status message field。 | [optional] 
**result_available** | **bool** | 字段 resultAvailable / result available field。 | 
**cancellable** | **bool** | 字段 cancellable / cancellable field。 | 
**failure_code** | **str** | 字段 failureCode / failure code field。 | [optional] 
**failure_message** | **str** | 字段 failureMessage / failure message field。 | [optional] 
**origin_conversation_id** | **str** | 字段 originConversationId / origin conversation id field。 | 
**origin_message_id** | **str** | 字段 originMessageId / origin message id field。 | 
**origin_tool_id** | **str** | 字段 originToolId / origin tool id field。 | 
**origin_tool_name** | **str** | 字段 originToolName / origin tool name field。 | 
**target_message_id** | **str** | 字段 targetMessageId / target message id field。 | 
**notification_status** | **str** | 字段 notificationStatus / notification status field。 | 
**notification_message_id** | **str** | 字段 notificationMessageId / notification message id field。 | [optional] 
**created_time** | **datetime** | 创建时间 / creation time。 | 
**started_time** | **datetime** | 字段 startedTime / started time field。 | [optional] 
**completed_time** | **datetime** | 字段 completedTime / completed time field。 | [optional] 
**last_update_time** | **datetime** | 最后更新时间 / last update time。 | 
**tracking_status** | **str** | 字段 trackingStatus / tracking status field。 | 
**tracking_failure_code** | **str** | 字段 trackingFailureCode / tracking failure code field。 | [optional] 
**last_poll_error** | **str** | 字段 lastPollError / last poll error field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.async_task import AsyncTask

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncTask from a JSON string
async_task_instance = AsyncTask.from_json(json)
# print the JSON string representation of the object
print(AsyncTask.to_json())

# convert the object into a dict
async_task_dict = async_task_instance.to_dict()
# create an instance of AsyncTask from a dict
async_task_from_dict = AsyncTask.from_dict(async_task_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


