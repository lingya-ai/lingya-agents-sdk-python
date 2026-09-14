# ChatModelConfig

ChatModelConfig 的公开协议结构。 / Public contract for chat model config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maker** | **str** | 字段 maker / maker field。 | 
**model_name** | **str** | 字段 modelName / model name field。 | 
**model_label** | **str** | 字段 modelLabel / model label field。 | 
**model_description** | **str** | 字段 modelDescription / model description field。 | 
**max_context_tokens** | **int** | 字段 maxContextTokens / max context tokens field。 | 
**max_output_tokens** | **int** | 字段 maxOutputTokens / max output tokens field。 | 
**support_image** | **bool** | 字段 supportImage / support image field。 | 
**support_video** | **bool** | 字段 supportVideo / support video field。 | 
**thinking_mode** | **bool** | 字段 thinkingMode / thinking mode field。 | 

## Example

```python
from lingya_agents_sdk.models.chat_model_config import ChatModelConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ChatModelConfig from a JSON string
chat_model_config_instance = ChatModelConfig.from_json(json)
# print the JSON string representation of the object
print(ChatModelConfig.to_json())

# convert the object into a dict
chat_model_config_dict = chat_model_config_instance.to_dict()
# create an instance of ChatModelConfig from a dict
chat_model_config_from_dict = ChatModelConfig.from_dict(chat_model_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


