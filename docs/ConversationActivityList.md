# ConversationActivityList

ConversationActivityList 的公开协议结构。 / Public contract for conversation activity list.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[ConversationActivity]**](ConversationActivity.md) | 记录列表 / records。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_activity_list import ConversationActivityList

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationActivityList from a JSON string
conversation_activity_list_instance = ConversationActivityList.from_json(json)
# print the JSON string representation of the object
print(ConversationActivityList.to_json())

# convert the object into a dict
conversation_activity_list_dict = conversation_activity_list_instance.to_dict()
# create an instance of ConversationActivityList from a dict
conversation_activity_list_from_dict = ConversationActivityList.from_dict(conversation_activity_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


