# SqlQueryResultPage

SqlQueryResultPage 的公开协议结构。 / Public contract for sql query result page.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_id** | **str** | 字段 resultId / result id field。 | 
**sql** | **str** | 字段 sql / sql field。 | 
**columns** | **List[str]** | 字段 columns / columns field。 | 
**row_count** | **int** | 字段 rowCount / row count field。 | 
**column_count** | **int** | 字段 columnCount / column count field。 | 
**current** | **int** | 字段 current / current field。 | 
**size** | **int** | 大小（字节）或分页容量 / byte size or page size。 | 
**total** | **int** | 字段 total / total field。 | 
**records** | [**List[SqlQueryResultRow]**](SqlQueryResultRow.md) | 记录列表 / records。 | 

## Example

```python
from lingya_agents_sdk.models.sql_query_result_page import SqlQueryResultPage

# TODO update the JSON string below
json = "{}"
# create an instance of SqlQueryResultPage from a JSON string
sql_query_result_page_instance = SqlQueryResultPage.from_json(json)
# print the JSON string representation of the object
print(SqlQueryResultPage.to_json())

# convert the object into a dict
sql_query_result_page_dict = sql_query_result_page_instance.to_dict()
# create an instance of SqlQueryResultPage from a dict
sql_query_result_page_from_dict = SqlQueryResultPage.from_dict(sql_query_result_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


