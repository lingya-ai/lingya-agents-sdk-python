# SqlChartResultExtensionToolExtension

SqlChartResultExtensionToolExtension 的公开协议结构。 / Public contract for sql chart result extension tool extension.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | 扩展类别判别值 / extension category discriminator。 | 
**content** | [**SqlChartResultExtensionContent**](SqlChartResultExtensionContent.md) | 与类别对应的强类型内容 / strongly typed content for the category。 | 
**special_render** | **bool** | 是否使用独立视图渲染 / whether to use a dedicated view。 | 

## Example

```python
from lingya_agents_sdk.models.sql_chart_result_extension_tool_extension import SqlChartResultExtensionToolExtension

# TODO update the JSON string below
json = "{}"
# create an instance of SqlChartResultExtensionToolExtension from a JSON string
sql_chart_result_extension_tool_extension_instance = SqlChartResultExtensionToolExtension.from_json(json)
# print the JSON string representation of the object
print(SqlChartResultExtensionToolExtension.to_json())

# convert the object into a dict
sql_chart_result_extension_tool_extension_dict = sql_chart_result_extension_tool_extension_instance.to_dict()
# create an instance of SqlChartResultExtensionToolExtension from a dict
sql_chart_result_extension_tool_extension_from_dict = SqlChartResultExtensionToolExtension.from_dict(sql_chart_result_extension_tool_extension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


