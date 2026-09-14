# AskUserQuestionOption

AskUserQuestionOption 的公开协议结构。 / Public contract for ask user question option.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | 字段 text / text field。 | 
**recommended** | **bool** | 字段 recommended / recommended field。 | 

## Example

```python
from lingya_agents_sdk.models.ask_user_question_option import AskUserQuestionOption

# TODO update the JSON string below
json = "{}"
# create an instance of AskUserQuestionOption from a JSON string
ask_user_question_option_instance = AskUserQuestionOption.from_json(json)
# print the JSON string representation of the object
print(AskUserQuestionOption.to_json())

# convert the object into a dict
ask_user_question_option_dict = ask_user_question_option_instance.to_dict()
# create an instance of AskUserQuestionOption from a dict
ask_user_question_option_from_dict = AskUserQuestionOption.from_dict(ask_user_question_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


