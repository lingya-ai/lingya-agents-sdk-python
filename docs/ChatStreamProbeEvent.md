# ChatStreamProbeEvent

ChatStreamProbeEvent 的公开协议结构。 / Public contract for chat stream probe event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**probe_id** | **str** | 字段 probeId / probe id field。 | 
**sequence** | **int** | 字段 sequence / sequence field。 | 
**server_elapsed_ms** | **int** | 字段 serverElapsedMs / server elapsed ms field。 | 

## Example

```python
from lingya_agents_sdk.models.chat_stream_probe_event import ChatStreamProbeEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ChatStreamProbeEvent from a JSON string
chat_stream_probe_event_instance = ChatStreamProbeEvent.from_json(json)
# print the JSON string representation of the object
print(ChatStreamProbeEvent.to_json())

# convert the object into a dict
chat_stream_probe_event_dict = chat_stream_probe_event_instance.to_dict()
# create an instance of ChatStreamProbeEvent from a dict
chat_stream_probe_event_from_dict = ChatStreamProbeEvent.from_dict(chat_stream_probe_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


