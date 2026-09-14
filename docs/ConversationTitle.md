# ConversationTitle

ConversationTitle 的公开协议结构。 / Public contract for conversation title.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | 会话 ID / conversation ID。 | 
**title** | **str** | 标题 / title。 | [optional] 
**title_state** | **str** | 字段 titleState / title state field。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_title import ConversationTitle

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationTitle from a JSON string
conversation_title_instance = ConversationTitle.from_json(json)
# print the JSON string representation of the object
print(ConversationTitle.to_json())

# convert the object into a dict
conversation_title_dict = conversation_title_instance.to_dict()
# create an instance of ConversationTitle from a dict
conversation_title_from_dict = ConversationTitle.from_dict(conversation_title_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


