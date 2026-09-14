# AskUserQuestionExtensionContent

AskUserQuestionExtensionContent 的公开协议结构。 / Public contract for ask user question extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**selected_options** | **List[str]** | 字段 selectedOptions / selected options field。 | 
**custom_input** | **str** | 字段 customInput / custom input field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.ask_user_question_extension_content import AskUserQuestionExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of AskUserQuestionExtensionContent from a JSON string
ask_user_question_extension_content_instance = AskUserQuestionExtensionContent.from_json(json)
# print the JSON string representation of the object
print(AskUserQuestionExtensionContent.to_json())

# convert the object into a dict
ask_user_question_extension_content_dict = ask_user_question_extension_content_instance.to_dict()
# create an instance of AskUserQuestionExtensionContent from a dict
ask_user_question_extension_content_from_dict = AskUserQuestionExtensionContent.from_dict(ask_user_question_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


