# AiChatFileRef

AiChatFileRef 的公开协议结构。 / Public contract for ai chat file ref.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 字段 id / id field。 | 
**file_name** | **str** | 文件名 / file name。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.ai_chat_file_ref import AiChatFileRef

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatFileRef from a JSON string
ai_chat_file_ref_instance = AiChatFileRef.from_json(json)
# print the JSON string representation of the object
print(AiChatFileRef.to_json())

# convert the object into a dict
ai_chat_file_ref_dict = ai_chat_file_ref_instance.to_dict()
# create an instance of AiChatFileRef from a dict
ai_chat_file_ref_from_dict = AiChatFileRef.from_dict(ai_chat_file_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


