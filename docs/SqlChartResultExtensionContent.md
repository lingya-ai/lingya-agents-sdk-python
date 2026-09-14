# SqlChartResultExtensionContent

SqlChartResultExtensionContent 的公开协议结构。 / Public contract for sql chart result extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_id** | **str** | 字段 resultId / result id field。 | 
**row_count** | **int** | 字段 rowCount / row count field。 | 
**column_count** | **int** | 字段 columnCount / column count field。 | 
**columns** | **List[str]** | 字段 columns / columns field。 | 
**var_schema** | [**List[SqlResultColumnSchema]**](SqlResultColumnSchema.md) | 字段 schema / schema field。 | 
**chart** | [**ChartSpec**](ChartSpec.md) | 字段 chart / chart field。 | 
**quality_summary** | [**ChartQualitySummary**](ChartQualitySummary.md) | 字段 qualitySummary / quality summary field。 | 
**time_context** | [**ChartTimeContext**](ChartTimeContext.md) | 字段 timeContext / time context field。 | 

## Example

```python
from lingya_agents_sdk.models.sql_chart_result_extension_content import SqlChartResultExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of SqlChartResultExtensionContent from a JSON string
sql_chart_result_extension_content_instance = SqlChartResultExtensionContent.from_json(json)
# print the JSON string representation of the object
print(SqlChartResultExtensionContent.to_json())

# convert the object into a dict
sql_chart_result_extension_content_dict = sql_chart_result_extension_content_instance.to_dict()
# create an instance of SqlChartResultExtensionContent from a dict
sql_chart_result_extension_content_from_dict = SqlChartResultExtensionContent.from_dict(sql_chart_result_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


