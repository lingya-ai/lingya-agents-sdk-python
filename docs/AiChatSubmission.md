# AiChatSubmission

AiChatSubmission 的公开协议结构。 / Public contract for ai chat submission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | 会话 ID / conversation ID。 | 
**message_id** | **str** | 消息 ID / message ID。 | 
**disposition** | **str** | 字段 disposition / disposition field。 Dispatch disposition. Unknown future values must be preserved. | 
**status** | **str** | 当前状态 / current status。 Persisted message status. Unknown future values must be preserved. | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_submission import AiChatSubmission

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatSubmission from a JSON string
ai_chat_submission_instance = AiChatSubmission.from_json(json)
# print the JSON string representation of the object
print(AiChatSubmission.to_json())

# convert the object into a dict
ai_chat_submission_dict = ai_chat_submission_instance.to_dict()
# create an instance of AiChatSubmission from a dict
ai_chat_submission_from_dict = AiChatSubmission.from_dict(ai_chat_submission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


