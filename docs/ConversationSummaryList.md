# ConversationSummaryList

ConversationSummaryList 的公开协议结构。 / Public contract for conversation summary list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[ConversationSummary]**](ConversationSummary.md) | 记录列表 / records。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_summary_list import ConversationSummaryList

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationSummaryList from a JSON string
conversation_summary_list_instance = ConversationSummaryList.from_json(json)
# print the JSON string representation of the object
print(ConversationSummaryList.to_json())

# convert the object into a dict
conversation_summary_list_dict = conversation_summary_list_instance.to_dict()
# create an instance of ConversationSummaryList from a dict
conversation_summary_list_from_dict = ConversationSummaryList.from_dict(conversation_summary_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


