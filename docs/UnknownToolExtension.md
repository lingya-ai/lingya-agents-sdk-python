# UnknownToolExtension

UnknownToolExtension 的公开协议结构。 / Public contract for unknown tool extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | 扩展类别判别值 / extension category discriminator。 | 
**raw_json** | **str** | 未识别对象的原始 JSON / raw JSON for an unrecognized object。 | 

## Example

```python
from lingya_agents_sdk.models.unknown_tool_extension import UnknownToolExtension

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownToolExtension from a JSON string
unknown_tool_extension_instance = UnknownToolExtension.from_json(json)
# print the JSON string representation of the object
print(UnknownToolExtension.to_json())

# convert the object into a dict
unknown_tool_extension_dict = unknown_tool_extension_instance.to_dict()
# create an instance of UnknownToolExtension from a dict
unknown_tool_extension_from_dict = UnknownToolExtension.from_dict(unknown_tool_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


