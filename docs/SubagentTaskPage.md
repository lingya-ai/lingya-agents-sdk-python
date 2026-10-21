# SubagentTaskPage

SubagentTaskPage 的公开协议结构。 / Public contract for subagent task page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[SubagentTask]**](SubagentTask.md) | 记录列表 / records。 |
**page** | [**PageInfo**](PageInfo.md) | 分页信息 / page metadata。 |

## Example

```python
from lingya_agents_sdk.models.subagent_task_page import SubagentTaskPage

# TODO update the JSON string below
json = "{}"
# create an instance of SubagentTaskPage from a JSON string
subagent_task_page_instance = SubagentTaskPage.from_json(json)
# print the JSON string representation of the object
print(SubagentTaskPage.to_json())

# convert the object into a dict
subagent_task_page_dict = subagent_task_page_instance.to_dict()
# create an instance of SubagentTaskPage from a dict
subagent_task_page_from_dict = SubagentTaskPage.from_dict(subagent_task_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


