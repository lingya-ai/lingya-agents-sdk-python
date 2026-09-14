# SkillResourceExtensionToolExtension

SkillResourceExtensionToolExtension 的公开协议结构。 / Public contract for skill resource extension tool extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | 扩展类别判别值 / extension category discriminator。 | 
**content** | [**SkillResourceExtensionContent**](SkillResourceExtensionContent.md) | 与类别对应的强类型内容 / strongly typed content for the category。 | 
**special_render** | **bool** | 是否使用独立视图渲染 / whether to use a dedicated view。 | 

## Example

```python
from lingya_agents_sdk.models.skill_resource_extension_tool_extension import SkillResourceExtensionToolExtension

# TODO update the JSON string below
json = "{}"
# create an instance of SkillResourceExtensionToolExtension from a JSON string
skill_resource_extension_tool_extension_instance = SkillResourceExtensionToolExtension.from_json(json)
# print the JSON string representation of the object
print(SkillResourceExtensionToolExtension.to_json())

# convert the object into a dict
skill_resource_extension_tool_extension_dict = skill_resource_extension_tool_extension_instance.to_dict()
# create an instance of SkillResourceExtensionToolExtension from a dict
skill_resource_extension_tool_extension_from_dict = SkillResourceExtensionToolExtension.from_dict(skill_resource_extension_tool_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


