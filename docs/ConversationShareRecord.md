# ConversationShareRecord

ConversationShareRecord 的公开协议结构。 / Public contract for conversation share record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**share_id** | **int** | 字段 shareId / share id field。 | 
**share_code** | **str** | 字段 shareCode / share code field。 | 
**server_name** | **str** | 字段 serverName / server name field。 | 
**access_mode** | **str** | 字段 accessMode / access mode field。 | 
**status** | **str** | 当前状态 / current status。 | 
**expires_at** | **datetime** | 字段 expiresAt / expires at field。 | [optional] 
**created_time** | **datetime** | 创建时间 / creation time。 | 
**last_update_time** | **datetime** | 最后更新时间 / last update time。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_share_record import ConversationShareRecord

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationShareRecord from a JSON string
conversation_share_record_instance = ConversationShareRecord.from_json(json)
# print the JSON string representation of the object
print(ConversationShareRecord.to_json())

# convert the object into a dict
conversation_share_record_dict = conversation_share_record_instance.to_dict()
# create an instance of ConversationShareRecord from a dict
conversation_share_record_from_dict = ConversationShareRecord.from_dict(conversation_share_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


