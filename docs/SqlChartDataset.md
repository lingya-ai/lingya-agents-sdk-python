# SqlChartDataset

SqlChartDataset 的公开协议结构。 / Public contract for sql chart dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_id** | **str** | 字段 resultId / result id field。 | 
**var_schema** | [**List[SqlResultColumnSchema]**](SqlResultColumnSchema.md) | 字段 schema / schema field。 | 
**row_count** | **int** | 字段 rowCount / row count field。 | 
**columns** | [**List[ChartColumnData]**](ChartColumnData.md) | 字段 columns / columns field。 | 

## Example

```python
from lingya_agents_sdk.models.sql_chart_dataset import SqlChartDataset

# TODO update the JSON string below
json = "{}"
# create an instance of SqlChartDataset from a JSON string
sql_chart_dataset_instance = SqlChartDataset.from_json(json)
# print the JSON string representation of the object
print(SqlChartDataset.to_json())

# convert the object into a dict
sql_chart_dataset_dict = sql_chart_dataset_instance.to_dict()
# create an instance of SqlChartDataset from a dict
sql_chart_dataset_from_dict = SqlChartDataset.from_dict(sql_chart_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


