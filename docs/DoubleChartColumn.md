# DoubleChartColumn

DoubleChartColumn 的公开协议结构。 / Public contract for double chart column.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 
**values** | **List[Optional[float]]** | 字段 values / values field。 | 

## Example

```python
from lingya_agents_sdk.models.double_chart_column import DoubleChartColumn

# TODO update the JSON string below
json = "{}"
# create an instance of DoubleChartColumn from a JSON string
double_chart_column_instance = DoubleChartColumn.from_json(json)
# print the JSON string representation of the object
print(DoubleChartColumn.to_json())

# convert the object into a dict
double_chart_column_dict = double_chart_column_instance.to_dict()
# create an instance of DoubleChartColumn from a dict
double_chart_column_from_dict = DoubleChartColumn.from_dict(double_chart_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


