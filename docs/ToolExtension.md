# ToolExtension

ToolExtension 的公开协议结构。 / Public contract for tool extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | 扩展类别判别值 / extension category discriminator。 | 
**content** | [**TaskProgressExtensionContent**](TaskProgressExtensionContent.md) | 与类别对应的强类型内容 / strongly typed content for the category。 | 
**special_render** | **bool** | 是否使用独立视图渲染 / whether to use a dedicated view。 | 
**raw_json** | **str** | 未识别对象的原始 JSON / raw JSON for an unrecognized object。 | 

## Example

```python
from lingya_agents_sdk.models.tool_extension import ToolExtension

# TODO update the JSON string below
json = "{}"
# create an instance of ToolExtension from a JSON string
tool_extension_instance = ToolExtension.from_json(json)
# print the JSON string representation of the object
print(ToolExtension.to_json())

# convert the object into a dict
tool_extension_dict = tool_extension_instance.to_dict()
# create an instance of ToolExtension from a dict
tool_extension_from_dict = ToolExtension.from_dict(tool_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


