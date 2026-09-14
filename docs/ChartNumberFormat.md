# ChartNumberFormat

ChartNumberFormat 的公开协议结构。 / Public contract for chart number format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | 类型判别值 / type discriminator。 | 
**currency** | **str** | 字段 currency / currency field。 | [optional] 
**decimal_places** | **int** | 字段 decimalPlaces / decimal places field。 | 
**value_scale** | **str** | 字段 valueScale / value scale field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.chart_number_format import ChartNumberFormat

# TODO update the JSON string below
json = "{}"
# create an instance of ChartNumberFormat from a JSON string
chart_number_format_instance = ChartNumberFormat.from_json(json)
# print the JSON string representation of the object
print(ChartNumberFormat.to_json())

# convert the object into a dict
chart_number_format_dict = chart_number_format_instance.to_dict()
# create an instance of ChartNumberFormat from a dict
chart_number_format_from_dict = ChartNumberFormat.from_dict(chart_number_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


