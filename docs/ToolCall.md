# ToolCall

ToolCall 的公开协议结构。 / Public contract for tool call.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 字段 id / id field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 
**name** | **str** | 字段 name / name field。 | 
**arguments** | **str** | 字段 arguments / arguments field。 | 

## Example

```python
from lingya_agents_sdk.models.tool_call import ToolCall

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCall from a JSON string
tool_call_instance = ToolCall.from_json(json)
# print the JSON string representation of the object
print(ToolCall.to_json())

# convert the object into a dict
tool_call_dict = tool_call_instance.to_dict()
# create an instance of ToolCall from a dict
tool_call_from_dict = ToolCall.from_dict(tool_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


