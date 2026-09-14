# ConversationShareList

ConversationShareList 的公开协议结构。 / Public contract for conversation share list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[ConversationShareRecord]**](ConversationShareRecord.md) | 记录列表 / records。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_share_list import ConversationShareList

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationShareList from a JSON string
conversation_share_list_instance = ConversationShareList.from_json(json)
# print the JSON string representation of the object
print(ConversationShareList.to_json())

# convert the object into a dict
conversation_share_list_dict = conversation_share_list_instance.to_dict()
# create an instance of ConversationShareList from a dict
conversation_share_list_from_dict = ConversationShareList.from_dict(conversation_share_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


