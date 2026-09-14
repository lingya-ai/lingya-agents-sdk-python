# Usage

Usage 的公开协议结构。 / Public contract for usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **int** | 输入 Token 数 / input token count。 | 
**output_tokens** | **int** | 输出 Token 数 / output token count。 | 
**total_tokens** | **int** | 总 Token 数 / total token count。 | [readonly] 
**input_token_breakdown** | [**InputTokenBreakdown**](InputTokenBreakdown.md) | 字段 inputTokenBreakdown / input token breakdown field。 | [optional] 
**reasoning_tokens** | **int** | 字段 reasoningTokens / reasoning tokens field。 | [optional] 
**cache_hit_rate** | **float** | 字段 cacheHitRate / cache hit rate field。 | [optional] [readonly] 
**input_breakdown_coverage_rate** | **float** | 字段 inputBreakdownCoverageRate / input breakdown coverage rate field。 | [optional] [readonly] 

## Example

```python
from lingya_agents_sdk.models.usage import Usage

# TODO update the JSON string below
json = "{}"
# create an instance of Usage from a JSON string
usage_instance = Usage.from_json(json)
# print the JSON string representation of the object
print(Usage.to_json())

# convert the object into a dict
usage_dict = usage_instance.to_dict()
# create an instance of Usage from a dict
usage_from_dict = Usage.from_dict(usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


