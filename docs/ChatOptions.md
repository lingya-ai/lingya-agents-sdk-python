# ChatOptions

ChatOptions 的公开协议结构。 / Public contract for chat options.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | 字段 model / model field。 | [optional] 
**frequency_penalty** | **float** | 字段 frequencyPenalty / frequency penalty field。 | [optional] 
**max_tokens** | **int** | 字段 maxTokens / max tokens field。 | [optional] 
**presence_penalty** | **float** | 字段 presencePenalty / presence penalty field。 | [optional] 
**stop_sequences** | **List[str]** | 字段 stopSequences / stop sequences field。 | [optional] 
**temperature** | **float** | 字段 temperature / temperature field。 | [optional] 
**top_p** | **float** | 字段 topP / top p field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.chat_options import ChatOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ChatOptions from a JSON string
chat_options_instance = ChatOptions.from_json(json)
# print the JSON string representation of the object
print(ChatOptions.to_json())

# convert the object into a dict
chat_options_dict = chat_options_instance.to_dict()
# create an instance of ChatOptions from a dict
chat_options_from_dict = ChatOptions.from_dict(chat_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


