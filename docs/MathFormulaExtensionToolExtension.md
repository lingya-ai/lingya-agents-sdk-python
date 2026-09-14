# MathFormulaExtensionToolExtension

MathFormulaExtensionToolExtension 的公开协议结构。 / Public contract for math formula extension tool extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | 扩展类别判别值 / extension category discriminator。 | 
**content** | [**MathFormulaExtensionContent**](MathFormulaExtensionContent.md) | 与类别对应的强类型内容 / strongly typed content for the category。 | 
**special_render** | **bool** | 是否使用独立视图渲染 / whether to use a dedicated view。 | 

## Example

```python
from lingya_agents_sdk.models.math_formula_extension_tool_extension import MathFormulaExtensionToolExtension

# TODO update the JSON string below
json = "{}"
# create an instance of MathFormulaExtensionToolExtension from a JSON string
math_formula_extension_tool_extension_instance = MathFormulaExtensionToolExtension.from_json(json)
# print the JSON string representation of the object
print(MathFormulaExtensionToolExtension.to_json())

# convert the object into a dict
math_formula_extension_tool_extension_dict = math_formula_extension_tool_extension_instance.to_dict()
# create an instance of MathFormulaExtensionToolExtension from a dict
math_formula_extension_tool_extension_from_dict = MathFormulaExtensionToolExtension.from_dict(math_formula_extension_tool_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


