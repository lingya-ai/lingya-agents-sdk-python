# lingya_agents_sdk.ChatApi

All URIs are relative to *https://tenant.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compact_conversation**](ChatApi.md#compact_conversation) | **POST** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/compact | 压缩会话上下文 / Compact conversation context
[**continue_chat**](ChatApi.md#continue_chat) | **POST** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId} | 向已有会话提交消息 / Submit a message to an existing conversation
[**create_chat**](ChatApi.md#create_chat) | **POST** /api/agents/channel/openapi/v1/{channelId}/chat | 创建会话并提交消息 / Create a conversation and submit a message
[**interrupt_conversation**](ChatApi.md#interrupt_conversation) | **DELETE** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/interrupt | 中断会话执行 / Interrupt conversation execution
[**probe_event_stream**](ChatApi.md#probe_event_stream) | **POST** /api/agents/channel/openapi/v1/{channelId}/chat/stream-probe | 探测 SSE 连接 / Probe the SSE connection
[**stream_chat_events**](ChatApi.md#stream_chat_events) | **POST** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/stream | 订阅消息事件流 / Stream message events


# **compact_conversation**
> compact_conversation(channel_id, conversation_id, force=force)

压缩会话上下文 / Compact conversation context

压缩会话上下文 / Compact conversation context 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tenant.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lingya_agents_sdk.Configuration(
    host = "https://tenant.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: OpenApiUser
configuration.api_key['OpenApiUser'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiUser'] = 'Bearer'

# Configure API key authorization: OpenApiAccessKey
configuration.api_key['OpenApiAccessKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiAccessKey'] = 'Bearer'

# Configure API key authorization: OpenApiTimestamp
configuration.api_key['OpenApiTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiTimestamp'] = 'Bearer'

# Configure API key authorization: OpenApiNonce
configuration.api_key['OpenApiNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiNonce'] = 'Bearer'

# Configure API key authorization: OpenApiSignature
configuration.api_key['OpenApiSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with lingya_agents_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lingya_agents_sdk.ChatApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    force = True # bool | 是否忽略当前阈值并强制压缩。 / Whether to compact regardless of the current threshold. (optional) (default to True)

    try:
        # 压缩会话上下文 / Compact conversation context
        api_instance.compact_conversation(channel_id, conversation_id, force=force)
    except Exception as e:
        print("Exception when calling ChatApi->compact_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **force** | **bool**| 是否忽略当前阈值并强制压缩。 / Whether to compact regardless of the current threshold. | [optional] [default to True]

### Return type

void (empty response body)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | 压缩会话上下文 / Compact conversation context 的成功响应。 / Successful response for compactConversation. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **continue_chat**
> AiChatSubmission continue_chat(channel_id, conversation_id, ai_chat_input)

向已有会话提交消息 / Submit a message to an existing conversation

向已有会话提交消息 / Submit a message to an existing conversation 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.ai_chat_input import AiChatInput
from lingya_agents_sdk.models.ai_chat_submission import AiChatSubmission
from lingya_agents_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tenant.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lingya_agents_sdk.Configuration(
    host = "https://tenant.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: OpenApiUser
configuration.api_key['OpenApiUser'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiUser'] = 'Bearer'

# Configure API key authorization: OpenApiAccessKey
configuration.api_key['OpenApiAccessKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiAccessKey'] = 'Bearer'

# Configure API key authorization: OpenApiTimestamp
configuration.api_key['OpenApiTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiTimestamp'] = 'Bearer'

# Configure API key authorization: OpenApiNonce
configuration.api_key['OpenApiNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiNonce'] = 'Bearer'

# Configure API key authorization: OpenApiSignature
configuration.api_key['OpenApiSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with lingya_agents_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lingya_agents_sdk.ChatApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    ai_chat_input = lingya_agents_sdk.AiChatInput() # AiChatInput | 向已有会话提交消息 / Submit a message to an existing conversation 的 JSON 请求参数。 / JSON request parameters for continueChat.

    try:
        # 向已有会话提交消息 / Submit a message to an existing conversation
        api_response = api_instance.continue_chat(channel_id, conversation_id, ai_chat_input)
        print("The response of ChatApi->continue_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->continue_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **ai_chat_input** | [**AiChatInput**](AiChatInput.md)| 向已有会话提交消息 / Submit a message to an existing conversation 的 JSON 请求参数。 / JSON request parameters for continueChat. | 

### Return type

[**AiChatSubmission**](AiChatSubmission.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 向已有会话提交消息 / Submit a message to an existing conversation 的成功响应。 / Successful response for continueChat. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chat**
> AiChatSubmission create_chat(channel_id, ai_chat_input)

创建会话并提交消息 / Create a conversation and submit a message

创建会话并提交消息 / Create a conversation and submit a message 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.ai_chat_input import AiChatInput
from lingya_agents_sdk.models.ai_chat_submission import AiChatSubmission
from lingya_agents_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tenant.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lingya_agents_sdk.Configuration(
    host = "https://tenant.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: OpenApiUser
configuration.api_key['OpenApiUser'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiUser'] = 'Bearer'

# Configure API key authorization: OpenApiAccessKey
configuration.api_key['OpenApiAccessKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiAccessKey'] = 'Bearer'

# Configure API key authorization: OpenApiTimestamp
configuration.api_key['OpenApiTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiTimestamp'] = 'Bearer'

# Configure API key authorization: OpenApiNonce
configuration.api_key['OpenApiNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiNonce'] = 'Bearer'

# Configure API key authorization: OpenApiSignature
configuration.api_key['OpenApiSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with lingya_agents_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lingya_agents_sdk.ChatApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    ai_chat_input = lingya_agents_sdk.AiChatInput() # AiChatInput | 创建会话并提交消息 / Create a conversation and submit a message 的 JSON 请求参数。 / JSON request parameters for createChat.

    try:
        # 创建会话并提交消息 / Create a conversation and submit a message
        api_response = api_instance.create_chat(channel_id, ai_chat_input)
        print("The response of ChatApi->create_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->create_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **ai_chat_input** | [**AiChatInput**](AiChatInput.md)| 创建会话并提交消息 / Create a conversation and submit a message 的 JSON 请求参数。 / JSON request parameters for createChat. | 

### Return type

[**AiChatSubmission**](AiChatSubmission.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 创建会话并提交消息 / Create a conversation and submit a message 的成功响应。 / Successful response for createChat. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interrupt_conversation**
> interrupt_conversation(channel_id, conversation_id)

中断会话执行 / Interrupt conversation execution

中断会话执行 / Interrupt conversation execution 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tenant.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lingya_agents_sdk.Configuration(
    host = "https://tenant.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: OpenApiUser
configuration.api_key['OpenApiUser'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiUser'] = 'Bearer'

# Configure API key authorization: OpenApiAccessKey
configuration.api_key['OpenApiAccessKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiAccessKey'] = 'Bearer'

# Configure API key authorization: OpenApiTimestamp
configuration.api_key['OpenApiTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiTimestamp'] = 'Bearer'

# Configure API key authorization: OpenApiNonce
configuration.api_key['OpenApiNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiNonce'] = 'Bearer'

# Configure API key authorization: OpenApiSignature
configuration.api_key['OpenApiSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with lingya_agents_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lingya_agents_sdk.ChatApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.

    try:
        # 中断会话执行 / Interrupt conversation execution
        api_instance.interrupt_conversation(channel_id, conversation_id)
    except Exception as e:
        print("Exception when calling ChatApi->interrupt_conversation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 

### Return type

void (empty response body)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 中断会话执行 / Interrupt conversation execution 的成功响应。 / Successful response for interruptConversation. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **probe_event_stream**
> ChatStreamProbeEvent probe_event_stream(channel_id, chat_stream_probe_input, x_request_id=x_request_id)

探测 SSE 连接 / Probe the SSE connection

探测 SSE 连接 / Probe the SSE connection 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.chat_stream_probe_event import ChatStreamProbeEvent
from lingya_agents_sdk.models.chat_stream_probe_input import ChatStreamProbeInput
from lingya_agents_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tenant.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lingya_agents_sdk.Configuration(
    host = "https://tenant.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: OpenApiUser
configuration.api_key['OpenApiUser'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiUser'] = 'Bearer'

# Configure API key authorization: OpenApiAccessKey
configuration.api_key['OpenApiAccessKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiAccessKey'] = 'Bearer'

# Configure API key authorization: OpenApiTimestamp
configuration.api_key['OpenApiTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiTimestamp'] = 'Bearer'

# Configure API key authorization: OpenApiNonce
configuration.api_key['OpenApiNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiNonce'] = 'Bearer'

# Configure API key authorization: OpenApiSignature
configuration.api_key['OpenApiSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with lingya_agents_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lingya_agents_sdk.ChatApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    chat_stream_probe_input = lingya_agents_sdk.ChatStreamProbeInput() # ChatStreamProbeInput | 探测 SSE 连接 / Probe the SSE connection 的 JSON 请求参数。 / JSON request parameters for probeEventStream.
    x_request_id = 'x_request_id_example' # str | 可选诊断请求 ID，便于关联客户端与服务端日志。 / Optional diagnostic request ID used to correlate client and server logs. (optional)

    try:
        # 探测 SSE 连接 / Probe the SSE connection
        api_response = api_instance.probe_event_stream(channel_id, chat_stream_probe_input, x_request_id=x_request_id)
        print("The response of ChatApi->probe_event_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->probe_event_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **chat_stream_probe_input** | [**ChatStreamProbeInput**](ChatStreamProbeInput.md)| 探测 SSE 连接 / Probe the SSE connection 的 JSON 请求参数。 / JSON request parameters for probeEventStream. | 
 **x_request_id** | **str**| 可选诊断请求 ID，便于关联客户端与服务端日志。 / Optional diagnostic request ID used to correlate client and server logs. | [optional] 

### Return type

[**ChatStreamProbeEvent**](ChatStreamProbeEvent.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server-Sent Events stream |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_chat_events**
> AiChatBriefEvent stream_chat_events(channel_id, conversation_id, ai_chat_stream_input, x_request_id=x_request_id)

订阅消息事件流 / Stream message events

订阅消息事件流 / Stream message events 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.ai_chat_brief_event import AiChatBriefEvent
from lingya_agents_sdk.models.ai_chat_stream_input import AiChatStreamInput
from lingya_agents_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://tenant.example.com
# See configuration.py for a list of all supported configuration parameters.
configuration = lingya_agents_sdk.Configuration(
    host = "https://tenant.example.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: OpenApiUser
configuration.api_key['OpenApiUser'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiUser'] = 'Bearer'

# Configure API key authorization: OpenApiAccessKey
configuration.api_key['OpenApiAccessKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiAccessKey'] = 'Bearer'

# Configure API key authorization: OpenApiTimestamp
configuration.api_key['OpenApiTimestamp'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiTimestamp'] = 'Bearer'

# Configure API key authorization: OpenApiNonce
configuration.api_key['OpenApiNonce'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiNonce'] = 'Bearer'

# Configure API key authorization: OpenApiSignature
configuration.api_key['OpenApiSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['OpenApiSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with lingya_agents_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lingya_agents_sdk.ChatApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    ai_chat_stream_input = lingya_agents_sdk.AiChatStreamInput() # AiChatStreamInput | 订阅消息事件流 / Stream message events 的 JSON 请求参数。 / JSON request parameters for streamChatEvents.
    x_request_id = 'x_request_id_example' # str | 可选诊断请求 ID，便于关联客户端与服务端日志。 / Optional diagnostic request ID used to correlate client and server logs. (optional)

    try:
        # 订阅消息事件流 / Stream message events
        api_response = api_instance.stream_chat_events(channel_id, conversation_id, ai_chat_stream_input, x_request_id=x_request_id)
        print("The response of ChatApi->stream_chat_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->stream_chat_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **ai_chat_stream_input** | [**AiChatStreamInput**](AiChatStreamInput.md)| 订阅消息事件流 / Stream message events 的 JSON 请求参数。 / JSON request parameters for streamChatEvents. | 
 **x_request_id** | **str**| 可选诊断请求 ID，便于关联客户端与服务端日志。 / Optional diagnostic request ID used to correlate client and server logs. | [optional] 

### Return type

[**AiChatBriefEvent**](AiChatBriefEvent.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Server-Sent Events stream |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

