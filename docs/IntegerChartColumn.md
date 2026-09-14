# IntegerChartColumn

IntegerChartColumn 的公开协议结构。 / Public contract for integer chart column.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 
**values** | **List[Optional[int]]** | 字段 values / values field。 | 

## Example

```python
from lingya_agents_sdk.models.integer_chart_column import IntegerChartColumn

# TODO update the JSON string below
json = "{}"
# create an instance of IntegerChartColumn from a JSON string
integer_chart_column_instance = IntegerChartColumn.from_json(json)
# print the JSON string representation of the object
print(IntegerChartColumn.to_json())

# convert the object into a dict
integer_chart_column_dict = integer_chart_column_instance.to_dict()
# create an instance of IntegerChartColumn from a dict
integer_chart_column_from_dict = IntegerChartColumn.from_dict(integer_chart_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


