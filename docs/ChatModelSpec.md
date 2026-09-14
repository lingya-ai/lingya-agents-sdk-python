# ChatModelSpec

ChatModelSpec 的公开协议结构。 / Public contract for chat model spec.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_group_id** | **int** | 字段 keyGroupId / key group id field。 | 
**model** | **str** | 字段 model / model field。 | 
**thinking** | **bool** | 字段 thinking / thinking field。 | [optional] 
**stop_sequences** | **List[str]** | 字段 stopSequences / stop sequences field。 | [optional] 
**temperature** | **float** | 字段 temperature / temperature field。 | [optional] 
**max_tokens** | **int** | 字段 maxTokens / max tokens field。 | [optional] 
**top_p** | **float** | 字段 topP / top p field。 | [optional] 
**top_k** | **int** | 字段 topK / top k field。 | [optional] 
**frequency_penalty** | **float** | 字段 frequencyPenalty / frequency penalty field。 | [optional] 
**presence_penalty** | **float** | 字段 presencePenalty / presence penalty field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.chat_model_spec import ChatModelSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ChatModelSpec from a JSON string
chat_model_spec_instance = ChatModelSpec.from_json(json)
# print the JSON string representation of the object
print(ChatModelSpec.to_json())

# convert the object into a dict
chat_model_spec_dict = chat_model_spec_instance.to_dict()
# create an instance of ChatModelSpec from a dict
chat_model_spec_from_dict = ChatModelSpec.from_dict(chat_model_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


