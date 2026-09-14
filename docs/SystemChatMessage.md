# SystemChatMessage

SystemChatMessage 的公开协议结构。 / Public contract for system chat message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**text** | **str** | 字段 text / text field。 | 
**metadata_raw_json** | **str** | 字段 metadataRawJson / metadata raw json field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.system_chat_message import SystemChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of SystemChatMessage from a JSON string
system_chat_message_instance = SystemChatMessage.from_json(json)
# print the JSON string representation of the object
print(SystemChatMessage.to_json())

# convert the object into a dict
system_chat_message_dict = system_chat_message_instance.to_dict()
# create an instance of SystemChatMessage from a dict
system_chat_message_from_dict = SystemChatMessage.from_dict(system_chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


