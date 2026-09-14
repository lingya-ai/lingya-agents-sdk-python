# MathFormulaExtensionContent

MathFormulaExtensionContent 的公开协议结构。 / Public contract for math formula extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expression** | **str** | 字段 expression / expression field。 | 
**variables** | [**List[VariableBinding]**](VariableBinding.md) | 字段 variables / variables field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.math_formula_extension_content import MathFormulaExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of MathFormulaExtensionContent from a JSON string
math_formula_extension_content_instance = MathFormulaExtensionContent.from_json(json)
# print the JSON string representation of the object
print(MathFormulaExtensionContent.to_json())

# convert the object into a dict
math_formula_extension_content_dict = math_formula_extension_content_instance.to_dict()
# create an instance of MathFormulaExtensionContent from a dict
math_formula_extension_content_from_dict = MathFormulaExtensionContent.from_dict(math_formula_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


