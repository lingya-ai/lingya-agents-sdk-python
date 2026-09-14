# ConversationContextUsage

ConversationContextUsage 的公开协议结构。 / Public contract for conversation context usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_prompt_tokens** | **int** | 字段 systemPromptTokens / system prompt tokens field。 | 
**session_message_tokens** | **int** | 字段 sessionMessageTokens / session message tokens field。 | 
**max_context_tokens** | **int** | 字段 maxContextTokens / max context tokens field。 | 
**tool_definition_tokens** | **int** | 字段 toolDefinitionTokens / tool definition tokens field。 | 
**protocol_reserve_tokens** | **int** | 字段 protocolReserveTokens / protocol reserve tokens field。 | 
**active_context_tokens** | **int** | 字段 activeContextTokens / active context tokens field。 | 
**requested_output_tokens** | **int** | 字段 requestedOutputTokens / requested output tokens field。 | 
**message_assembly_reserve_tokens** | **int** | 字段 messageAssemblyReserveTokens / message assembly reserve tokens field。 | 
**required_context_tokens** | **int** | 字段 requiredContextTokens / required context tokens field。 | 
**active_usage_ratio** | **float** | 字段 activeUsageRatio / active usage ratio field。 | [optional] 
**required_usage_ratio** | **float** | 字段 requiredUsageRatio / required usage ratio field。 | [optional] 
**calculation_source** | **str** | 字段 calculationSource / calculation source field。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_context_usage import ConversationContextUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationContextUsage from a JSON string
conversation_context_usage_instance = ConversationContextUsage.from_json(json)
# print the JSON string representation of the object
print(ConversationContextUsage.to_json())

# convert the object into a dict
conversation_context_usage_dict = conversation_context_usage_instance.to_dict()
# create an instance of ConversationContextUsage from a dict
conversation_context_usage_from_dict = ConversationContextUsage.from_dict(conversation_context_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


