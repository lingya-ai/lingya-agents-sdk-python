# JsRunScriptResultExtensionContent

JsRunScriptResultExtensionContent 的公开协议结构。 / Public contract for js run script result extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | 字段 result / result field。 | [optional] 
**stdout** | **str** | 字段 stdout / stdout field。 | 

## Example

```python
from lingya_agents_sdk.models.js_run_script_result_extension_content import JsRunScriptResultExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of JsRunScriptResultExtensionContent from a JSON string
js_run_script_result_extension_content_instance = JsRunScriptResultExtensionContent.from_json(json)
# print the JSON string representation of the object
print(JsRunScriptResultExtensionContent.to_json())

# convert the object into a dict
js_run_script_result_extension_content_dict = js_run_script_result_extension_content_instance.to_dict()
# create an instance of JsRunScriptResultExtensionContent from a dict
js_run_script_result_extension_content_from_dict = JsRunScriptResultExtensionContent.from_dict(js_run_script_result_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


