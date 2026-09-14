# StringChartColumn

StringChartColumn 的公开协议结构。 / Public contract for string chart column.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 
**values** | **List[Optional[str]]** | 字段 values / values field。 | 

## Example

```python
from lingya_agents_sdk.models.string_chart_column import StringChartColumn

# TODO update the JSON string below
json = "{}"
# create an instance of StringChartColumn from a JSON string
string_chart_column_instance = StringChartColumn.from_json(json)
# print the JSON string representation of the object
print(StringChartColumn.to_json())

# convert the object into a dict
string_chart_column_dict = string_chart_column_instance.to_dict()
# create an instance of StringChartColumn from a dict
string_chart_column_from_dict = StringChartColumn.from_dict(string_chart_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


