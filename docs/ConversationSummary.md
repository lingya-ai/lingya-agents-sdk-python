# ConversationSummary

ConversationSummary 的公开协议结构。 / Public contract for conversation summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | 会话 ID / conversation ID。 | 
**conversation_type** | **str** | 字段 conversationType / conversation type field。 | 
**title** | **str** | 标题 / title。 | [optional] 
**title_state** | **str** | 字段 titleState / title state field。 | 
**status** | **str** | 当前状态 / current status。 | 
**message_count** | **int** | 字段 messageCount / message count field。 | 
**total_tokens** | **int** | 总 Token 数 / total token count。 | 
**total_input_tokens** | **int** | 字段 totalInputTokens / total input tokens field。 | 
**total_output_tokens** | **int** | 字段 totalOutputTokens / total output tokens field。 | 
**usage** | [**Usage**](Usage.md) | 字段 usage / usage field。 | 
**created_time** | **datetime** | 创建时间 / creation time。 | 
**last_update_time** | **datetime** | 最后更新时间 / last update time。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_summary import ConversationSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationSummary from a JSON string
conversation_summary_instance = ConversationSummary.from_json(json)
# print the JSON string representation of the object
print(ConversationSummary.to_json())

# convert the object into a dict
conversation_summary_dict = conversation_summary_instance.to_dict()
# create an instance of ConversationSummary from a dict
conversation_summary_from_dict = ConversationSummary.from_dict(conversation_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


