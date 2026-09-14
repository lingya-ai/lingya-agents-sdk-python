# SqlQueryResultRow

SqlQueryResultRow 的公开协议结构。 / Public contract for sql query result row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | **List[Optional[str]]** | 字段 values / values field。 | 

## Example

```python
from lingya_agents_sdk.models.sql_query_result_row import SqlQueryResultRow

# TODO update the JSON string below
json = "{}"
# create an instance of SqlQueryResultRow from a JSON string
sql_query_result_row_instance = SqlQueryResultRow.from_json(json)
# print the JSON string representation of the object
print(SqlQueryResultRow.to_json())

# convert the object into a dict
sql_query_result_row_dict = sql_query_result_row_instance.to_dict()
# create an instance of SqlQueryResultRow from a dict
sql_query_result_row_from_dict = SqlQueryResultRow.from_dict(sql_query_result_row_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


