# LocalDateChartColumn

LocalDateChartColumn 的公开协议结构。 / Public contract for local date chart column.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 
**values** | **List[Optional[date]]** | 字段 values / values field。 | 

## Example

```python
from lingya_agents_sdk.models.local_date_chart_column import LocalDateChartColumn

# TODO update the JSON string below
json = "{}"
# create an instance of LocalDateChartColumn from a JSON string
local_date_chart_column_instance = LocalDateChartColumn.from_json(json)
# print the JSON string representation of the object
print(LocalDateChartColumn.to_json())

# convert the object into a dict
local_date_chart_column_dict = local_date_chart_column_instance.to_dict()
# create an instance of LocalDateChartColumn from a dict
local_date_chart_column_from_dict = LocalDateChartColumn.from_dict(local_date_chart_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


