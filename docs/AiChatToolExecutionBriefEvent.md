# AiChatToolExecutionBriefEvent

AiChatToolExecutionBriefEvent 的公开协议结构。 / Public contract for ai chat tool execution brief event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**tool_id** | **str** | 字段 toolId / tool id field。 | 
**tool_name** | **str** | 字段 toolName / tool name field。 | 
**status** | **str** | 当前状态 / current status。 | 
**action** | **str** | 字段 action / action field。 | 
**summary** | **str** | 字段 summary / summary field。 | [optional] 
**extension** | [**ToolExtension**](ToolExtension.md) | 字段 extension / extension field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.ai_chat_tool_execution_brief_event import AiChatToolExecutionBriefEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatToolExecutionBriefEvent from a JSON string
ai_chat_tool_execution_brief_event_instance = AiChatToolExecutionBriefEvent.from_json(json)
# print the JSON string representation of the object
print(AiChatToolExecutionBriefEvent.to_json())

# convert the object into a dict
ai_chat_tool_execution_brief_event_dict = ai_chat_tool_execution_brief_event_instance.to_dict()
# create an instance of AiChatToolExecutionBriefEvent from a dict
ai_chat_tool_execution_brief_event_from_dict = AiChatToolExecutionBriefEvent.from_dict(ai_chat_tool_execution_brief_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


