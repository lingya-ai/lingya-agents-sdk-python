# InstantChartColumn

InstantChartColumn 的公开协议结构。 / Public contract for instant chart column.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 
**values** | **List[Optional[datetime]]** | 字段 values / values field。 | 

## Example

```python
from lingya_agents_sdk.models.instant_chart_column import InstantChartColumn

# TODO update the JSON string below
json = "{}"
# create an instance of InstantChartColumn from a JSON string
instant_chart_column_instance = InstantChartColumn.from_json(json)
# print the JSON string representation of the object
print(InstantChartColumn.to_json())

# convert the object into a dict
instant_chart_column_dict = instant_chart_column_instance.to_dict()
# create an instance of InstantChartColumn from a dict
instant_chart_column_from_dict = InstantChartColumn.from_dict(instant_chart_column_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


