# LocalDateTimeChartColumn

LocalDateTimeChartColumn 的公开协议结构。 / Public contract for local date time chart column.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 
**values** | **List[Optional[str]]** | 字段 values / values field。 | 

## Example

```python
from lingya_agents_sdk.models.local_date_time_chart_column import LocalDateTimeChartColumn

# TODO update the JSON string below
json = "{}"
# create an instance of LocalDateTimeChartColumn from a JSON string
local_date_time_chart_column_instance = LocalDateTimeChartColumn.from_json(json)
# print the JSON string representation of the object
print(LocalDateTimeChartColumn.to_json())

# convert the object into a dict
local_date_time_chart_column_dict = local_date_time_chart_column_instance.to_dict()
# create an instance of LocalDateTimeChartColumn from a dict
local_date_time_chart_column_from_dict = LocalDateTimeChartColumn.from_dict(local_date_time_chart_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


