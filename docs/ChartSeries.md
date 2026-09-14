# ChartSeries

ChartSeries 的公开协议结构。 / Public contract for chart series.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 | 
**value_column** | **str** | 字段 valueColumn / value column field。 | 
**render_type** | **str** | 字段 renderType / render type field。 | 
**axis** | **str** | 字段 axis / axis field。 | 
**number_format** | [**ChartNumberFormat**](ChartNumberFormat.md) | 字段 numberFormat / number format field。 | 
**stack** | **str** | 字段 stack / stack field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.chart_series import ChartSeries

# TODO update the JSON string below
json = "{}"
# create an instance of ChartSeries from a JSON string
chart_series_instance = ChartSeries.from_json(json)
# print the JSON string representation of the object
print(ChartSeries.to_json())

# convert the object into a dict
chart_series_dict = chart_series_instance.to_dict()
# create an instance of ChartSeries from a dict
chart_series_from_dict = ChartSeries.from_dict(chart_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


