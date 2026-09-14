# PageInfo

PageInfo 的公开协议结构。 / Public contract for page info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | **int** | 字段 current / current field。 | 
**size** | **int** | 大小（字节）或分页容量 / byte size or page size。 | 
**total** | **int** | 字段 total / total field。 | 

## Example

```python
from lingya_agents_sdk.models.page_info import PageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PageInfo from a JSON string
page_info_instance = PageInfo.from_json(json)
# print the JSON string representation of the object
print(PageInfo.to_json())

# convert the object into a dict
page_info_dict = page_info_instance.to_dict()
# create an instance of PageInfo from a dict
page_info_from_dict = PageInfo.from_dict(page_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


