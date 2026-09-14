# ConversationShareCreated

ConversationShareCreated 的公开协议结构。 / Public contract for conversation share created.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_id** | **int** | 字段 shareId / share id field。 | 
**share_code** | **str** | 字段 shareCode / share code field。 | 
**server_name** | **str** | 字段 serverName / server name field。 | 
**password_required** | **bool** | 字段 passwordRequired / password required field。 | 
**expires_at** | **datetime** | 字段 expiresAt / expires at field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.conversation_share_created import ConversationShareCreated

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationShareCreated from a JSON string
conversation_share_created_instance = ConversationShareCreated.from_json(json)
# print the JSON string representation of the object
print(ConversationShareCreated.to_json())

# convert the object into a dict
conversation_share_created_dict = conversation_share_created_instance.to_dict()
# create an instance of ConversationShareCreated from a dict
conversation_share_created_from_dict = ConversationShareCreated.from_dict(conversation_share_created_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


