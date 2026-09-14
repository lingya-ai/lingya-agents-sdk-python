# InputTokenBreakdown

InputTokenBreakdown 的公开协议结构。 / Public contract for input token breakdown.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**observed_input_tokens** | **int** | 字段 observedInputTokens / observed input tokens field。 | 
**uncached_input_tokens** | **int** | 字段 uncachedInputTokens / uncached input tokens field。 | 
**cached_input_tokens** | **int** | 字段 cachedInputTokens / cached input tokens field。 | 
**cache_creation_input_tokens** | **int** | 字段 cacheCreationInputTokens / cache creation input tokens field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.input_token_breakdown import InputTokenBreakdown

# TODO update the JSON string below
json = "{}"
# create an instance of InputTokenBreakdown from a JSON string
input_token_breakdown_instance = InputTokenBreakdown.from_json(json)
# print the JSON string representation of the object
print(InputTokenBreakdown.to_json())

# convert the object into a dict
input_token_breakdown_dict = input_token_breakdown_instance.to_dict()
# create an instance of InputTokenBreakdown from a dict
input_token_breakdown_from_dict = InputTokenBreakdown.from_dict(input_token_breakdown_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


