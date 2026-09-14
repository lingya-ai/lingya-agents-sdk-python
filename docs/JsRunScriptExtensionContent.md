# JsRunScriptExtensionContent

JsRunScriptExtensionContent 的公开协议结构。 / Public contract for js run script extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** | 字段 script / script field。 | 

## Example

```python
from lingya_agents_sdk.models.js_run_script_extension_content import JsRunScriptExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of JsRunScriptExtensionContent from a JSON string
js_run_script_extension_content_instance = JsRunScriptExtensionContent.from_json(json)
# print the JSON string representation of the object
print(JsRunScriptExtensionContent.to_json())

# convert the object into a dict
js_run_script_extension_content_dict = js_run_script_extension_content_instance.to_dict()
# create an instance of JsRunScriptExtensionContent from a dict
js_run_script_extension_content_from_dict = JsRunScriptExtensionContent.from_dict(js_run_script_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


