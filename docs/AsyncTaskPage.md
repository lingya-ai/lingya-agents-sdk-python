# AsyncTaskPage

AsyncTaskPage 的公开协议结构。 / Public contract for async task page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[AsyncTask]**](AsyncTask.md) | 记录列表 / records。 | 
**page** | [**PageInfo**](PageInfo.md) | 分页信息 / page metadata。 | 

## Example

```python
from lingya_agents_sdk.models.async_task_page import AsyncTaskPage

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncTaskPage from a JSON string
async_task_page_instance = AsyncTaskPage.from_json(json)
# print the JSON string representation of the object
print(AsyncTaskPage.to_json())

# convert the object into a dict
async_task_page_dict = async_task_page_instance.to_dict()
# create an instance of AsyncTaskPage from a dict
async_task_page_from_dict = AsyncTaskPage.from_dict(async_task_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


