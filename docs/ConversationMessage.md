# ConversationMessage

ConversationMessage 的公开协议结构。 / Public contract for conversation message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | 消息 ID / message ID。 | 
**user_message** | [**ConversationUserMessage**](ConversationUserMessage.md) | 字段 userMessage / user message field。 | 
**input_tokens** | **int** | 输入 Token 数 / input token count。 | 
**output_tokens** | **int** | 输出 Token 数 / output token count。 | 
**total_tokens** | **int** | 总 Token 数 / total token count。 | 
**usage** | [**Usage**](Usage.md) | 字段 usage / usage field。 | 
**execution_time_millis** | **int** | 字段 executionTimeMillis / execution time millis field。 | 
**processing_steps** | **int** | 字段 processingSteps / processing steps field。 | 
**total_tool_calls** | **int** | 字段 totalToolCalls / total tool calls field。 | 
**status** | **str** | 当前状态 / current status。 | 
**created_time** | **datetime** | 创建时间 / creation time。 | 
**last_update_time** | **datetime** | 最后更新时间 / last update time。 | 
**execution_type** | **str** | 字段 executionType / execution type field。 | 
**parent_message_id** | **str** | 字段 parentMessageId / parent message id field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.conversation_message import ConversationMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessage from a JSON string
conversation_message_instance = ConversationMessage.from_json(json)
# print the JSON string representation of the object
print(ConversationMessage.to_json())

# convert the object into a dict
conversation_message_dict = conversation_message_instance.to_dict()
# create an instance of ConversationMessage from a dict
conversation_message_from_dict = ConversationMessage.from_dict(conversation_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


