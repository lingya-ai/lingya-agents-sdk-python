# PlanApprovalInput

PlanApprovalInput 的公开协议结构。 / Public contract for plan approval input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | 会话 ID / conversation ID。 | 
**message_id** | **str** | 消息 ID / message ID。 | 
**approved** | **bool** | 字段 approved / approved field。 | 
**feedback** | **str** | 字段 feedback / feedback field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.plan_approval_input import PlanApprovalInput

# TODO update the JSON string below
json = "{}"
# create an instance of PlanApprovalInput from a JSON string
plan_approval_input_instance = PlanApprovalInput.from_json(json)
# print the JSON string representation of the object
print(PlanApprovalInput.to_json())

# convert the object into a dict
plan_approval_input_dict = plan_approval_input_instance.to_dict()
# create an instance of PlanApprovalInput from a dict
plan_approval_input_from_dict = PlanApprovalInput.from_dict(plan_approval_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


