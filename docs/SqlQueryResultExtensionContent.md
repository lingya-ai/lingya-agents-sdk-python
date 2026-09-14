# SqlQueryResultExtensionContent

SqlQueryResultExtensionContent 的公开协议结构。 / Public contract for sql query result extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_id** | **str** | 字段 resultId / result id field。 | 
**row_count** | **int** | 字段 rowCount / row count field。 | 
**total_row_count** | **int** | 字段 totalRowCount / total row count field。 | 
**column_count** | **int** | 字段 columnCount / column count field。 | 
**columns** | **List[str]** | 字段 columns / columns field。 | 
**var_schema** | [**List[SqlResultColumnSchema]**](SqlResultColumnSchema.md) | 字段 schema / schema field。 | 
**truncated** | **bool** | 字段 truncated / truncated field。 | 
**limit** | **int** | 字段 limit / limit field。 | 

## Example

```python
from lingya_agents_sdk.models.sql_query_result_extension_content import SqlQueryResultExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of SqlQueryResultExtensionContent from a JSON string
sql_query_result_extension_content_instance = SqlQueryResultExtensionContent.from_json(json)
# print the JSON string representation of the object
print(SqlQueryResultExtensionContent.to_json())

# convert the object into a dict
sql_query_result_extension_content_dict = sql_query_result_extension_content_instance.to_dict()
# create an instance of SqlQueryResultExtensionContent from a dict
sql_query_result_extension_content_from_dict = SqlQueryResultExtensionContent.from_dict(sql_query_result_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


