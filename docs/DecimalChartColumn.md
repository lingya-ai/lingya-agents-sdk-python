# DecimalChartColumn

DecimalChartColumn 的公开协议结构。 / Public contract for decimal chart column.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 
**values** | **List[Optional[str]]** | 字段 values / values field。 | 

## Example

```python
from lingya_agents_sdk.models.decimal_chart_column import DecimalChartColumn

# TODO update the JSON string below
json = "{}"
# create an instance of DecimalChartColumn from a JSON string
decimal_chart_column_instance = DecimalChartColumn.from_json(json)
# print the JSON string representation of the object
print(DecimalChartColumn.to_json())

# convert the object into a dict
decimal_chart_column_dict = decimal_chart_column_instance.to_dict()
# create an instance of DecimalChartColumn from a dict
decimal_chart_column_from_dict = DecimalChartColumn.from_dict(decimal_chart_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


