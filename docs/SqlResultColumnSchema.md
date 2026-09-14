# SqlResultColumnSchema

SqlResultColumnSchema 的公开协议结构。 / Public contract for sql result column schema.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | 字段 name / name field。 | 
**type** | **str** | 类型判别值 / type discriminator。 | 
**nullable** | **bool** | 字段 nullable / nullable field。 | 
**precision** | **int** | 字段 precision / precision field。 | [optional] 
**scale** | **int** | 字段 scale / scale field。 | [optional] 

## Example

```python
from lingya_agents_sdk.models.sql_result_column_schema import SqlResultColumnSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SqlResultColumnSchema from a JSON string
sql_result_column_schema_instance = SqlResultColumnSchema.from_json(json)
# print the JSON string representation of the object
print(SqlResultColumnSchema.to_json())

# convert the object into a dict
sql_result_column_schema_dict = sql_result_column_schema_instance.to_dict()
# create an instance of SqlResultColumnSchema from a dict
sql_result_column_schema_from_dict = SqlResultColumnSchema.from_dict(sql_result_column_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


