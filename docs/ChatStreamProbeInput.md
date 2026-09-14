# ChatStreamProbeInput

ChatStreamProbeInput 的公开协议结构。 / Public contract for chat stream probe input.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**probe_id** | **str** | 字段 probeId / probe id field。 | 

## Example

```python
from lingya_agents_sdk.models.chat_stream_probe_input import ChatStreamProbeInput

# TODO update the JSON string below
json = "{}"
# create an instance of ChatStreamProbeInput from a JSON string
chat_stream_probe_input_instance = ChatStreamProbeInput.from_json(json)
# print the JSON string representation of the object
print(ChatStreamProbeInput.to_json())

# convert the object into a dict
chat_stream_probe_input_dict = chat_stream_probe_input_instance.to_dict()
# create an instance of ChatStreamProbeInput from a dict
chat_stream_probe_input_from_dict = ChatStreamProbeInput.from_dict(chat_stream_probe_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


