# AiChatSubAgentCallBriefEvent

AiChatSubAgentCallBriefEvent 的公开协议结构。 / Public contract for ai chat sub agent call brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**tool_call_id** | **str** | 字段 toolCallId / tool call id field。 | 
**tool_name** | **str** | 字段 toolName / tool name field。 | 
**sub_agent_conversation_id** | **str** | 字段 subAgentConversationId / sub agent conversation id field。 | 
**sub_agent_message_id** | **str** | 字段 subAgentMessageId / sub agent message id field。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_sub_agent_call_brief_event import AiChatSubAgentCallBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatSubAgentCallBriefEvent from a JSON string
ai_chat_sub_agent_call_brief_event_instance = AiChatSubAgentCallBriefEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatSubAgentCallBriefEvent.to_json())

# convert the object into a dict
ai_chat_sub_agent_call_brief_event_dict = ai_chat_sub_agent_call_brief_event_instance.to_dict()
# create an instance of AiChatSubAgentCallBriefEvent from a dict
ai_chat_sub_agent_call_brief_event_from_dict = AiChatSubAgentCallBriefEvent.from_dict(ai_chat_sub_agent_call_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


