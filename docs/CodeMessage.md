# CodeMessage

CodeMessage 的公开协议结构。 / Public contract for code message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | 字段 code / code field。 | 
**message** | **str** | 消息正文 / message text。 | 

## Example

```python
from lingya_agents_sdk.models.code_message import CodeMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CodeMessage from a JSON string
code_message_instance = CodeMessage.from_json(json)
# print the JSON string representation of the object
print(CodeMessage.to_json())

# convert the object into a dict
code_message_dict = code_message_instance.to_dict()
# create an instance of CodeMessage from a dict
code_message_from_dict = CodeMessage.from_dict(code_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


