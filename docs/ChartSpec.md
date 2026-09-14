# ChartSpec

ChartSpec 的公开协议结构。 / Public contract for chart spec.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | 字段 version / version field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 
**title** | **str** | 标题 / title。 | 
**subtitle** | **str** | 字段 subtitle / subtitle field。 | [optional] 
**category_column** | **str** | 字段 categoryColumn / category column field。 | 
**category_type** | **str** | 字段 categoryType / category type field。 | 
**orientation** | **str** | 字段 orientation / orientation field。 | 
**series** | [**List[ChartSeries]**](ChartSeries.md) | 字段 series / series field。 | 
**legend** | **bool** | 字段 legend / legend field。 | 
**data_zoom** | **str** | 字段 dataZoom / data zoom field。 | 
**null_policy** | **str** | 字段 nullPolicy / null policy field。 | 

## Example

```python
from lingya_agents_sdk.models.chart_spec import ChartSpec

# TODO update the JSON string below
json = "{}"
# create an instance of ChartSpec from a JSON string
chart_spec_instance = ChartSpec.from_json(json)
# print the JSON string representation of the object
print(ChartSpec.to_json())

# convert the object into a dict
chart_spec_dict = chart_spec_instance.to_dict()
# create an instance of ChartSpec from a dict
chart_spec_from_dict = ChartSpec.from_dict(chart_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


