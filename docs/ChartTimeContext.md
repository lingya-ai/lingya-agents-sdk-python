# ChartTimeContext

ChartTimeContext 的公开协议结构。 / Public contract for chart time context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_of_instant** | **datetime** | 字段 asOfInstant / as of instant field。 | 
**tenant_zone_id** | **str** | 字段 tenantZoneId / tenant zone id field。 | 

## Example

```python
from lingya_agents_sdk.models.chart_time_context import ChartTimeContext

# TODO update the JSON string below
json = "{}"
# create an instance of ChartTimeContext from a JSON string
chart_time_context_instance = ChartTimeContext.from_json(json)
# print the JSON string representation of the object
print(ChartTimeContext.to_json())

# convert the object into a dict
chart_time_context_dict = chart_time_context_instance.to_dict()
# create an instance of ChartTimeContext from a dict
chart_time_context_from_dict = ChartTimeContext.from_dict(chart_time_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


