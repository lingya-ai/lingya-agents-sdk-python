# PlanApprovalExtensionContent

PlanApprovalExtensionContent 的公开协议结构。 / Public contract for plan approval extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preview_file_id** | **int** | 字段 previewFileId / preview file id field。 | 
**server_now** | **datetime** | 字段 serverNow / server now field。 | 
**approval_timeout_at** | **datetime** | 字段 approvalTimeoutAt / approval timeout at field。 | 

## Example

```python
from lingya_agents_sdk.models.plan_approval_extension_content import PlanApprovalExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of PlanApprovalExtensionContent from a JSON string
plan_approval_extension_content_instance = PlanApprovalExtensionContent.from_json(json)
# print the JSON string representation of the object
print(PlanApprovalExtensionContent.to_json())

# convert the object into a dict
plan_approval_extension_content_dict = plan_approval_extension_content_instance.to_dict()
# create an instance of PlanApprovalExtensionContent from a dict
plan_approval_extension_content_from_dict = PlanApprovalExtensionContent.from_dict(plan_approval_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


