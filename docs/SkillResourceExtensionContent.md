# SkillResourceExtensionContent

SkillResourceExtensionContent 的公开协议结构。 / Public contract for skill resource extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation_type** | **str** | 字段 operationType / operation type field。 | 
**filepath** | **str** | 字段 filepath / filepath field。 | 

## Example

```python
from lingya_agents_sdk.models.skill_resource_extension_content import SkillResourceExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of SkillResourceExtensionContent from a JSON string
skill_resource_extension_content_instance = SkillResourceExtensionContent.from_json(json)
# print the JSON string representation of the object
print(SkillResourceExtensionContent.to_json())

# convert the object into a dict
skill_resource_extension_content_dict = skill_resource_extension_content_instance.to_dict()
# create an instance of SkillResourceExtensionContent from a dict
skill_resource_extension_content_from_dict = SkillResourceExtensionContent.from_dict(skill_resource_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


