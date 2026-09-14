# ChartQualitySummary

ChartQualitySummary 的公开协议结构。 / Public contract for chart quality summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**null_value_count** | **int** | 字段 nullValueCount / null value count field。 | 
**null_value_columns** | **List[str]** | 字段 nullValueColumns / null value columns field。 | 
**zero_filled_value_count** | **int** | 字段 zeroFilledValueCount / zero filled value count field。 | 

## Example

```python
from lingya_agents_sdk.models.chart_quality_summary import ChartQualitySummary

# TODO update the JSON string below
json = "{}"
# create an instance of ChartQualitySummary from a JSON string
chart_quality_summary_instance = ChartQualitySummary.from_json(json)
# print the JSON string representation of the object
print(ChartQualitySummary.to_json())

# convert the object into a dict
chart_quality_summary_dict = chart_quality_summary_instance.to_dict()
# create an instance of ChartQualitySummary from a dict
chart_quality_summary_from_dict = ChartQualitySummary.from_dict(chart_quality_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


