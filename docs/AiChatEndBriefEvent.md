# AiChatEndBriefEvent

AiChatEndBriefEvent 的公开协议结构。 / Public contract for ai chat end brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**execution_time_millis** | **int** | 字段 executionTimeMillis / execution time millis field。 | 
**total_usage** | [**Usage**](Usage.md) | 字段 totalUsage / total usage field。 | 
**message_context_usage_ratio** | **float** | 字段 messageContextUsageRatio / message context usage ratio field。 | [optional] 
**context_window_usage** | [**ConversationContextUsage**](ConversationContextUsage.md) | 字段 contextWindowUsage / context window usage field。 | [optional] 
**artifacts** | [**List[ArtifactInfo]**](ArtifactInfo.md) | 字段 artifacts / artifacts field。 | 
**non_file_artifacts** | [**List[WorkspaceNonFileArtifact]**](WorkspaceNonFileArtifact.md) | 字段 nonFileArtifacts / non file artifacts field。 | 

## Example

```python
from lingya_agents_sdk.models.ai_chat_end_brief_event import AiChatEndBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatEndBriefEvent from a JSON string
ai_chat_end_brief_event_instance = AiChatEndBriefEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatEndBriefEvent.to_json())

# convert the object into a dict
ai_chat_end_brief_event_dict = ai_chat_end_brief_event_instance.to_dict()
# create an instance of AiChatEndBriefEvent from a dict
ai_chat_end_brief_event_from_dict = AiChatEndBriefEvent.from_dict(ai_chat_end_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


