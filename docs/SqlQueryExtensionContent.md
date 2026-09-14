# SqlQueryExtensionContent

SqlQueryExtensionContent 的公开协议结构。 / Public contract for sql query extension content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sql** | **str** | 字段 sql / sql field。 | 

## Example

```python
from lingya_agents_sdk.models.sql_query_extension_content import SqlQueryExtensionContent

# TODO update the JSON string below
json = "{}"
# create an instance of SqlQueryExtensionContent from a JSON string
sql_query_extension_content_instance = SqlQueryExtensionContent.from_json(json)
# print the JSON string representation of the object
print(SqlQueryExtensionContent.to_json())

# convert the object into a dict
sql_query_extension_content_dict = sql_query_extension_content_instance.to_dict()
# create an instance of SqlQueryExtensionContent from a dict
sql_query_extension_content_from_dict = SqlQueryExtensionContent.from_dict(sql_query_extension_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


