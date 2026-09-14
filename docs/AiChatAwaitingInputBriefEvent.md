# AiChatAwaitingInputBriefEvent

AiChatAwaitingInputBriefEvent 的公开协议结构。 / Public contract for ai chat awaiting input brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**tool_call_id** | **str** | 字段 toolCallId / tool call id field。 | 
**tool_name** | **str** | 字段 toolName / tool name field。 | 
**question_id** | **str** | 字段 questionId / question id field。 | 
**question** | **str** | 字段 question / question field。 | 
**options** | [**List[AskUserQuestionOption]**](AskUserQuestionOption.md) | 字段 options / options field。 | 
**multiple** | **bool** | 字段 multiple / multiple field。 | 
**server_now** | **datetime** | 字段 serverNow / server now field。 | 
**timeout_seconds** | **int** | 字段 timeoutSeconds / timeout seconds field。 | 
**question_details** | **str** | 字段 questionDetails / question details field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.ai_chat_awaiting_input_brief_event import AiChatAwaitingInputBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatAwaitingInputBriefEvent from a JSON string
ai_chat_awaiting_input_brief_event_instance = AiChatAwaitingInputBriefEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatAwaitingInputBriefEvent.to_json())

# convert the object into a dict
ai_chat_awaiting_input_brief_event_dict = ai_chat_awaiting_input_brief_event_instance.to_dict()
# create an instance of AiChatAwaitingInputBriefEvent from a dict
ai_chat_awaiting_input_brief_event_from_dict = AiChatAwaitingInputBriefEvent.from_dict(ai_chat_awaiting_input_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


