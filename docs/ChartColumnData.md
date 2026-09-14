# ChartColumnData

ChartColumnData 的公开协议结构。 / Public contract for chart column data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 
**values** | **List[datetime]** | 字段 values / values field。 | 

## Example

```python
from lingya_agents_sdk.models.chart_column_data import ChartColumnData

# TODO update the JSON string below
json = "{}"
# create an instance of ChartColumnData from a JSON string
chart_column_data_instance = ChartColumnData.from_json(json)
# print the JSON string representation of the object
print(ChartColumnData.to_json())

# convert the object into a dict
chart_column_data_dict = chart_column_data_instance.to_dict()
# create an instance of ChartColumnData from a dict
chart_column_data_from_dict = ChartColumnData.from_dict(chart_column_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


