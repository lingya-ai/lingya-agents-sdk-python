# ToolResponseChatMessage

ToolResponseChatMessage 的公开协议结构。 / Public contract for tool response chat message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**responses** | [**List[ToolResponse]**](ToolResponse.md) | 字段 responses / responses field。 | 
**metadata_raw_json** | **str** | 字段 metadataRawJson / metadata raw json field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.tool_response_chat_message import ToolResponseChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ToolResponseChatMessage from a JSON string
tool_response_chat_message_instance = ToolResponseChatMessage.from_json(json)
# print the JSON string representation of the object
print(ToolResponseChatMessage.to_json())

# convert the object into a dict
tool_response_chat_message_dict = tool_response_chat_message_instance.to_dict()
# create an instance of ToolResponseChatMessage from a dict
tool_response_chat_message_from_dict = ToolResponseChatMessage.from_dict(tool_response_chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


