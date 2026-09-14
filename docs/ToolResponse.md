# ToolResponse

ToolResponse 的公开协议结构。 / Public contract for tool response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | 字段 id / id field。 | 
**name** | **str** | 字段 name / name field。 | 
**status** | **str** | 当前状态 / current status。 | 
**response_data** | **str** | 字段 responseData / response data field。 | 
**metadata_raw_json** | **str** | 字段 metadataRawJson / metadata raw json field。 | 

## Example

```python
from lingya_agents_sdk.models.tool_response import ToolResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ToolResponse from a JSON string
tool_response_instance = ToolResponse.from_json(json)
# print the JSON string representation of the object
print(ToolResponse.to_json())

# convert the object into a dict
tool_response_dict = tool_response_instance.to_dict()
# create an instance of ToolResponse from a dict
tool_response_from_dict = ToolResponse.from_dict(tool_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


