# ConversationGroupNameInput

ConversationGroupNameInput 的公开协议结构。 / Public contract for conversation group name input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 |

## Example

```python
from lingya_agents_sdk.models.conversation_group_name_input import ConversationGroupNameInput

# TODO update the JSON string below
json = "{}"
# create an instance of ConversationGroupNameInput from a JSON string
conversation_group_name_input_instance = ConversationGroupNameInput.from_json(json)
# print the JSON string representation of the object
print(ConversationGroupNameInput.to_json())

# convert the object into a dict
conversation_group_name_input_dict = conversation_group_name_input_instance.to_dict()
# create an instance of ConversationGroupNameInput from a dict
conversation_group_name_input_from_dict = ConversationGroupNameInput.from_dict(conversation_group_name_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


