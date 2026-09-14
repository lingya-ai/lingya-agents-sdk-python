# MathResultExtensionContent

MathResultExtensionContent 的公开协议结构。 / Public contract for math result extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | 字段 result / result field。 | 

## Example

```python
from lingya_agents_sdk.models.math_result_extension_content import MathResultExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of MathResultExtensionContent from a JSON string
math_result_extension_content_instance = MathResultExtensionContent.from_json(json)
# print the JSON string representation of the object
print(MathResultExtensionContent.to_json())

# convert the object into a dict
math_result_extension_content_dict = math_result_extension_content_instance.to_dict()
# create an instance of MathResultExtensionContent from a dict
math_result_extension_content_from_dict = MathResultExtensionContent.from_dict(math_result_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


