# UserInputAnswerInput

UserInputAnswerInput 的公开协议结构。 / Public contract for user input answer input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conversation_id** | **str** | 会话 ID / conversation ID。 | 
**message_id** | **str** | 消息 ID / message ID。 | 
**question_id** | **str** | 字段 questionId / question id field。 | 
**selected_options** | **List[str]** | 字段 selectedOptions / selected options field。 | 
**custom_input** | **str** | 字段 customInput / custom input field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.user_input_answer_input import UserInputAnswerInput

# TODO update the JSON string below
json = "{}"
# create an instance of UserInputAnswerInput from a JSON string
user_input_answer_input_instance = UserInputAnswerInput.from_json(json)
# print the JSON string representation of the object
print(UserInputAnswerInput.to_json())

# convert the object into a dict
user_input_answer_input_dict = user_input_answer_input_instance.to_dict()
# create an instance of UserInputAnswerInput from a dict
user_input_answer_input_from_dict = UserInputAnswerInput.from_dict(user_input_answer_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


