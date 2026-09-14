# ConversationShareRevoked

ConversationShareRevoked 的公开协议结构。 / Public contract for conversation share revoked.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_id** | **int** | 字段 shareId / share id field。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_share_revoked import ConversationShareRevoked

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationShareRevoked from a JSON string
conversation_share_revoked_instance = ConversationShareRevoked.from_json(json)
# print the JSON string representation of the object
print(ConversationShareRevoked.to_json())

# convert the object into a dict
conversation_share_revoked_dict = conversation_share_revoked_instance.to_dict()
# create an instance of ConversationShareRevoked from a dict
conversation_share_revoked_from_dict = ConversationShareRevoked.from_dict(conversation_share_revoked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


