# UpdateConversationGroupInput

UpdateConversationGroupInput 的公开协议结构。 / Public contract for update conversation group input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **int** | 字段 groupId / group id field。 |

## Example

```python
from lingya_agents_sdk.models.update_conversation_group_input import UpdateConversationGroupInput

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConversationGroupInput from a JSON string
update_conversation_group_input_instance = UpdateConversationGroupInput.from_json(json)
# print the JSON string representation of the object
print(UpdateConversationGroupInput.to_json())

# convert the object into a dict
update_conversation_group_input_dict = update_conversation_group_input_instance.to_dict()
# create an instance of UpdateConversationGroupInput from a dict
update_conversation_group_input_from_dict = UpdateConversationGroupInput.from_dict(update_conversation_group_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


