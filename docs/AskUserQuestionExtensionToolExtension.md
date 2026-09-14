# AskUserQuestionExtensionToolExtension

AskUserQuestionExtensionToolExtension 的公开协议结构。 / Public contract for ask user question extension tool extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | 扩展类别判别值 / extension category discriminator。 | 
**content** | [**AskUserQuestionExtensionContent**](AskUserQuestionExtensionContent.md) | 与类别对应的强类型内容 / strongly typed content for the category。 | 
**special_render** | **bool** | 是否使用独立视图渲染 / whether to use a dedicated view。 | 

## Example

```python
from lingya_agents_sdk.models.ask_user_question_extension_tool_extension import AskUserQuestionExtensionToolExtension

# TODO update the JSON string below
json = "{}"
# create an instance of AskUserQuestionExtensionToolExtension from a JSON string
ask_user_question_extension_tool_extension_instance = AskUserQuestionExtensionToolExtension.from_json(json)
# print the JSON string representation of the object
print(AskUserQuestionExtensionToolExtension.to_json())

# convert the object into a dict
ask_user_question_extension_tool_extension_dict = ask_user_question_extension_tool_extension_instance.to_dict()
# create an instance of AskUserQuestionExtensionToolExtension from a dict
ask_user_question_extension_tool_extension_from_dict = AskUserQuestionExtensionToolExtension.from_dict(ask_user_question_extension_tool_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


