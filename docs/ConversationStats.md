# ConversationStats

ConversationStats 的公开协议结构。 / Public contract for conversation stats.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publish_id** | **str** | 字段 publishId / publish id field。 | 
**total_conversations** | **int** | 字段 totalConversations / total conversations field。 | 
**active_conversations** | **int** | 字段 activeConversations / active conversations field。 | 
**total_messages** | **int** | 字段 totalMessages / total messages field。 | 
**total_tokens** | **int** | 总 Token 数 / total token count。 | 
**avg_messages_per_conversation** | **float** | 字段 avgMessagesPerConversation / avg messages per conversation field。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_stats import ConversationStats

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationStats from a JSON string
conversation_stats_instance = ConversationStats.from_json(json)
# print the JSON string representation of the object
print(ConversationStats.to_json())

# convert the object into a dict
conversation_stats_dict = conversation_stats_instance.to_dict()
# create an instance of ConversationStats from a dict
conversation_stats_from_dict = ConversationStats.from_dict(conversation_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


