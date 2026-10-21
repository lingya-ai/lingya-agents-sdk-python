# ConversationMessageSync

ConversationMessageSync 的公开协议结构。 / Public contract for conversation message sync.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**List[ConversationMessage]**](ConversationMessage.md) | 字段 messages / messages field。 |
**next_message_id** | **str** | 字段 nextMessageId / next message id field。 |
**has_more** | **bool** | 字段 hasMore / has more field。 |

## Example

```python
from lingya_agents_sdk.models.conversation_message_sync import ConversationMessageSync

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationMessageSync from a JSON string
conversation_message_sync_instance = ConversationMessageSync.from_json(json)
# print the JSON string representation of the object
print(ConversationMessageSync.to_json())

# convert the object into a dict
conversation_message_sync_dict = conversation_message_sync_instance.to_dict()
# create an instance of ConversationMessageSync from a dict
conversation_message_sync_from_dict = ConversationMessageSync.from_dict(conversation_message_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


