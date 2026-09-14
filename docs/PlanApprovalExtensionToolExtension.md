# PlanApprovalExtensionToolExtension

PlanApprovalExtensionToolExtension 的公开协议结构。 / Public contract for plan approval extension tool extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | 扩展类别判别值 / extension category discriminator。 | 
**content** | [**PlanApprovalExtensionContent**](PlanApprovalExtensionContent.md) | 与类别对应的强类型内容 / strongly typed content for the category。 | 
**special_render** | **bool** | 是否使用独立视图渲染 / whether to use a dedicated view。 | 

## Example

```python
from lingya_agents_sdk.models.plan_approval_extension_tool_extension import PlanApprovalExtensionToolExtension

# TODO update the JSON string below
json = "{}"
# create an instance of PlanApprovalExtensionToolExtension from a JSON string
plan_approval_extension_tool_extension_instance = PlanApprovalExtensionToolExtension.from_json(json)
# print the JSON string representation of the object
print(PlanApprovalExtensionToolExtension.to_json())

# convert the object into a dict
plan_approval_extension_tool_extension_dict = plan_approval_extension_tool_extension_instance.to_dict()
# create an instance of PlanApprovalExtensionToolExtension from a dict
plan_approval_extension_tool_extension_from_dict = PlanApprovalExtensionToolExtension.from_dict(plan_approval_extension_tool_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


