# PlanStatus

PlanStatus 的公开协议结构。 / Public contract for plan status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending** | **bool** | 字段 pending / pending field。 | 
**status** | **str** | 当前状态 / current status。 | 

## Example

```python
from lingya_agents_sdk.models.plan_status import PlanStatus

# TODO update the JSON string below
json = "{}"
# create an instance of PlanStatus from a JSON string
plan_status_instance = PlanStatus.from_json(json)
# print the JSON string representation of the object
print(PlanStatus.to_json())

# convert the object into a dict
plan_status_dict = plan_status_instance.to_dict()
# create an instance of PlanStatus from a dict
plan_status_from_dict = PlanStatus.from_dict(plan_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


