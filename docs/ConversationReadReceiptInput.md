# ConversationReadReceiptInput

ConversationReadReceiptInput 的公开协议结构。 / Public contract for conversation read receipt input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** | 消息 ID / message ID。 | 

## Example

```python
from lingya_agents_sdk.models.conversation_read_receipt_input import ConversationReadReceiptInput

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationReadReceiptInput from a JSON string
conversation_read_receipt_input_instance = ConversationReadReceiptInput.from_json(json)
# print the JSON string representation of the object
print(ConversationReadReceiptInput.to_json())

# convert the object into a dict
conversation_read_receipt_input_dict = conversation_read_receipt_input_instance.to_dict()
# create an instance of ConversationReadReceiptInput from a dict
conversation_read_receipt_input_from_dict = ConversationReadReceiptInput.from_dict(conversation_read_receipt_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


