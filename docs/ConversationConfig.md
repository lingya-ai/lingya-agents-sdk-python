# ConversationConfig

ConversationConfig 的公开协议结构。 / Public contract for conversation config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_chat_model_spec** | [**ChatModelSpec**](ChatModelSpec.md) | 字段 lastChatModelSpec / last chat model spec field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.conversation_config import ConversationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationConfig from a JSON string
conversation_config_instance = ConversationConfig.from_json(json)
# print the JSON string representation of the object
print(ConversationConfig.to_json())

# convert the object into a dict
conversation_config_dict = conversation_config_instance.to_dict()
# create an instance of ConversationConfig from a dict
conversation_config_from_dict = ConversationConfig.from_dict(conversation_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


