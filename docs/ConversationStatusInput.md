# ConversationStatusInput

ConversationStatusInput 的公开协议结构。 / Public contract for conversation status input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | 当前状态 / current status。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_status_input import ConversationStatusInput

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationStatusInput from a JSON string
conversation_status_input_instance = ConversationStatusInput.from_json(json)
# print the JSON string representation of the object
print(ConversationStatusInput.to_json())

# convert the object into a dict
conversation_status_input_dict = conversation_status_input_instance.to_dict()
# create an instance of ConversationStatusInput from a dict
conversation_status_input_from_dict = ConversationStatusInput.from_dict(conversation_status_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


