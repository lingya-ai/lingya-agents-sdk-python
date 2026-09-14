# AgentFile

AgentFile 的公开协议结构。 / Public contract for agent file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | 字段 id / id field。 | 
**file_name** | **str** | 文件名 / file name。 | 
**content_md5** | **str** | 字段 contentMd5 / content md5 field。 | 
**size** | **int** | 大小（字节）或分页容量 / byte size or page size。 | 
**created_time** | **datetime** | 创建时间 / creation time。 | 
**last_update_time** | **datetime** | 最后更新时间 / last update time。 | 

## Example

```python
from lingya_agents_sdk.models.agent_file import AgentFile

# TODO update the JSON string below
json = "{}"
# create an instance of AgentFile from a JSON string
agent_file_instance = AgentFile.from_json(json)
# print the JSON string representation of the object
print(AgentFile.to_json())

# convert the object into a dict
agent_file_dict = agent_file_instance.to_dict()
# create an instance of AgentFile from a dict
agent_file_from_dict = AgentFile.from_dict(agent_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


