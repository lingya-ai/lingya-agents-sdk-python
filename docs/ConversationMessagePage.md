# ConversationMessagePage

ConversationMessagePage 的公开协议结构。 / Public contract for conversation message page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**records** | [**List[ConversationMessage]**](ConversationMessage.md) | 记录列表 / records。 | 
**page** | [**PageInfo**](PageInfo.md) | 分页信息 / page metadata。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_message_page import ConversationMessagePage

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessagePage from a JSON string
conversation_message_page_instance = ConversationMessagePage.from_json(json)
# print the JSON string representation of the object
print(ConversationMessagePage.to_json())

# convert the object into a dict
conversation_message_page_dict = conversation_message_page_instance.to_dict()
# create an instance of ConversationMessagePage from a dict
conversation_message_page_from_dict = ConversationMessagePage.from_dict(conversation_message_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


