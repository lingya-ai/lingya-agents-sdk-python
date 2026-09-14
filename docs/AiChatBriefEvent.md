# AiChatBriefEvent

AiChatBriefEvent 的公开协议结构。 / Public contract for ai chat brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**query** | **str** | 用户问题 / user query。 | 
**attachments** | [**List[MediaAttachment]**](MediaAttachment.md) | 字段 attachments / attachments field。 | [optional] 
**level** | **str** | 字段 level / level field。 | 
**warning** | **str** | 字段 warning / warning field。 | 
**message** | **str** | 消息正文 / message text。 | 
**messages** | [**List[ChatMessage]**](ChatMessage.md) | 字段 messages / messages field。 | 
**chat_options** | [**ChatOptions**](ChatOptions.md) | 字段 chatOptions / chat options field。 | [optional] 
**assistant_messages** | [**List[AssistantChatMessage]**](AssistantChatMessage.md) | 字段 assistantMessages / assistant messages field。 | 
**usage** | [**Usage**](Usage.md) | 字段 usage / usage field。 | 
**tool_id** | **str** | 字段 toolId / tool id field。 | 
**tool_name** | **str** | 字段 toolName / tool name field。 | 
**status** | **str** | 当前状态 / current status。 | 
**action** | **str** | 字段 action / action field。 | 
**summary** | **str** | 字段 summary / summary field。 | [optional] 
**extension** | [**ToolExtension**](ToolExtension.md) | 字段 extension / extension field。 | [optional] 
**tool_call_id** | **str** | 字段 toolCallId / tool call id field。 | 
**sub_agent_conversation_id** | **str** | 字段 subAgentConversationId / sub agent conversation id field。 | 
**sub_agent_message_id** | **str** | 字段 subAgentMessageId / sub agent message id field。 | 
**question_id** | **str** | 字段 questionId / question id field。 | 
**question** | **str** | 字段 question / question field。 | 
**options** | [**List[AskUserQuestionOption]**](AskUserQuestionOption.md) | 字段 options / options field。 | 
**multiple** | **bool** | 字段 multiple / multiple field。 | 
**server_now** | **datetime** | 字段 serverNow / server now field。 | 
**timeout_seconds** | **int** | 字段 timeoutSeconds / timeout seconds field。 | 
**question_details** | **str** | 字段 questionDetails / question details field。 | [optional] 
**execution_time_millis** | **int** | 字段 executionTimeMillis / execution time millis field。 | 
**total_usage** | [**Usage**](Usage.md) | 字段 totalUsage / total usage field。 | 
**message_context_usage_ratio** | **float** | 字段 messageContextUsageRatio / message context usage ratio field。 | [optional] 
**context_window_usage** | [**ConversationContextUsage**](ConversationContextUsage.md) | 字段 contextWindowUsage / context window usage field。 | [optional] 
**artifacts** | [**List[ArtifactInfo]**](ArtifactInfo.md) | 字段 artifacts / artifacts field。 | 
**non_file_artifacts** | [**List[WorkspaceNonFileArtifact]**](WorkspaceNonFileArtifact.md) | 字段 nonFileArtifacts / non file artifacts field。 | 
**raw_json** | **str** | 未识别对象的原始 JSON / raw JSON for an unrecognized object。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_brief_event import AiChatBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatBriefEvent from a JSON string
ai_chat_brief_event_instance = AiChatBriefEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatBriefEvent.to_json())

# convert the object into a dict
ai_chat_brief_event_dict = ai_chat_brief_event_instance.to_dict()
# create an instance of AiChatBriefEvent from a dict
ai_chat_brief_event_from_dict = AiChatBriefEvent.from_dict(ai_chat_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


