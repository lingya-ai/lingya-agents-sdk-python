# ConversationActivity

ConversationActivity 的公开协议结构。 / Public contract for conversation activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | 会话 ID / conversation ID。 | 
**execution_status** | **str** | 字段 executionStatus / execution status field。 | 
**active_message_id** | **str** | 字段 activeMessageId / active message id field。 | [optional] 
**execution_epoch** | **str** | 字段 executionEpoch / execution epoch field。 | [optional] 
**execution_started_time** | **datetime** | 字段 executionStartedTime / execution started time field。 | [optional] 
**latest_terminal_message_id** | **str** | 字段 latestTerminalMessageId / latest terminal message id field。 | [optional] 
**latest_terminal_time** | **datetime** | 字段 latestTerminalTime / latest terminal time field。 | [optional] 
**has_unread_completion** | **bool** | 字段 hasUnreadCompletion / has unread completion field。 | 
**requires_user_confirmation** | **bool** | 字段 requiresUserConfirmation / requires user confirmation field。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_activity import ConversationActivity

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationActivity from a JSON string
conversation_activity_instance = ConversationActivity.from_json(json)
# print the JSON string representation of the object
print(ConversationActivity.to_json())

# convert the object into a dict
conversation_activity_dict = conversation_activity_instance.to_dict()
# create an instance of ConversationActivity from a dict
conversation_activity_from_dict = ConversationActivity.from_dict(conversation_activity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


