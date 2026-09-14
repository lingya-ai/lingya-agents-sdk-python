# ConversationShareInput

ConversationShareInput 的公开协议结构。 / Public contract for conversation share input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | 字段 password / password field。 | [optional] 
**expires_at** | **datetime** | 字段 expiresAt / expires at field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.conversation_share_input import ConversationShareInput

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationShareInput from a JSON string
conversation_share_input_instance = ConversationShareInput.from_json(json)
# print the JSON string representation of the object
print(ConversationShareInput.to_json())

# convert the object into a dict
conversation_share_input_dict = conversation_share_input_instance.to_dict()
# create an instance of ConversationShareInput from a dict
conversation_share_input_from_dict = ConversationShareInput.from_dict(conversation_share_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


