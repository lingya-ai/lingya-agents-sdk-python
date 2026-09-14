# ConversationTitleInput

ConversationTitleInput 的公开协议结构。 / Public contract for conversation title input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | 标题 / title。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_title_input import ConversationTitleInput

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationTitleInput from a JSON string
conversation_title_input_instance = ConversationTitleInput.from_json(json)
# print the JSON string representation of the object
print(ConversationTitleInput.to_json())

# convert the object into a dict
conversation_title_input_dict = conversation_title_input_instance.to_dict()
# create an instance of ConversationTitleInput from a dict
conversation_title_input_from_dict = ConversationTitleInput.from_dict(conversation_title_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


