# lingya_agents_sdk.MessagesApi

All URIs are relative to *https://tenant.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_queued_message**](MessagesApi.md#cancel_queued_message) | **DELETE** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/messages/{messageId}/queue | 取消排队消息 / Cancel a queued message
[**get_conversation_async_task**](MessagesApi.md#get_conversation_async_task) | **GET** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/async-tasks/{asyncTaskId} | 读取异步任务 / Get an asynchronous task
[**get_conversation_message**](MessagesApi.md#get_conversation_message) | **GET** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/messages/{messageId} | 读取单条会话消息 / Get a conversation message
[**list_conversation_async_tasks**](MessagesApi.md#list_conversation_async_tasks) | **GET** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/async-tasks | 分页查询异步任务 / List asynchronous tasks
[**list_conversation_messages**](MessagesApi.md#list_conversation_messages) | **GET** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/messages | 分页查询会话消息 / List conversation messages


# **cancel_queued_message**
> ConversationMessage cancel_queued_message(channel_id, conversation_id, message_id)

取消排队消息 / Cancel a queued message

取消排队消息 / Cancel a queued message 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.conversation_message import ConversationMessage
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
    api_instance = lingya_agents_sdk.MessagesApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    message_id = 'message_id_example' # str | 用户消息 ID；必须属于指定会话。 / User-message ID owned by the specified conversation.

    try:
        # 取消排队消息 / Cancel a queued message
        api_response = api_instance.cancel_queued_message(channel_id, conversation_id, message_id)
        print("The response of MessagesApi->cancel_queued_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->cancel_queued_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **message_id** | **str**| 用户消息 ID；必须属于指定会话。 / User-message ID owned by the specified conversation. | 

### Return type

[**ConversationMessage**](ConversationMessage.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 取消排队消息 / Cancel a queued message 的成功响应。 / Successful response for cancelQueuedMessage. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_async_task**
> AsyncTask get_conversation_async_task(channel_id, conversation_id, async_task_id)

读取异步任务 / Get an asynchronous task

读取异步任务 / Get an asynchronous task 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.async_task import AsyncTask
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
    api_instance = lingya_agents_sdk.MessagesApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    async_task_id = 'async_task_id_example' # str | 异步任务 ID。 / Asynchronous task ID.

    try:
        # 读取异步任务 / Get an asynchronous task
        api_response = api_instance.get_conversation_async_task(channel_id, conversation_id, async_task_id)
        print("The response of MessagesApi->get_conversation_async_task:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_conversation_async_task: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **async_task_id** | **str**| 异步任务 ID。 / Asynchronous task ID. | 

### Return type

[**AsyncTask**](AsyncTask.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 读取异步任务 / Get an asynchronous task 的成功响应。 / Successful response for getConversationAsyncTask. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_message**
> ConversationMessage get_conversation_message(channel_id, conversation_id, message_id)

读取单条会话消息 / Get a conversation message

读取单条会话消息 / Get a conversation message 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.conversation_message import ConversationMessage
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
    api_instance = lingya_agents_sdk.MessagesApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    message_id = 'message_id_example' # str | 用户消息 ID；必须属于指定会话。 / User-message ID owned by the specified conversation.

    try:
        # 读取单条会话消息 / Get a conversation message
        api_response = api_instance.get_conversation_message(channel_id, conversation_id, message_id)
        print("The response of MessagesApi->get_conversation_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->get_conversation_message: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **message_id** | **str**| 用户消息 ID；必须属于指定会话。 / User-message ID owned by the specified conversation. | 

### Return type

[**ConversationMessage**](ConversationMessage.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 读取单条会话消息 / Get a conversation message 的成功响应。 / Successful response for getConversationMessage. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conversation_async_tasks**
> AsyncTaskPage list_conversation_async_tasks(channel_id, conversation_id, current=current, size=size, order_by=order_by, order_direction=order_direction, order_null_handling=order_null_handling, keyword=keyword, status=status)

分页查询异步任务 / List asynchronous tasks

分页查询异步任务 / List asynchronous tasks 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.async_task_page import AsyncTaskPage
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
    api_instance = lingya_agents_sdk.MessagesApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    current = 56 # int | 从 0 开始的页码。 / Zero-based page index. (optional)
    size = 30 # int | 单页记录数。 / Number of records per page. (optional) (default to 30)
    order_by = ['order_by_example'] # List[str] | 排序字段列表。 / Ordered list of sort fields. (optional)
    order_direction = 'ASC' # str | 排序方向。 / Sort direction. (optional) (default to 'ASC')
    order_null_handling = 'NATIVE' # str | 空值排序策略。 / Null ordering strategy. (optional) (default to 'NATIVE')
    keyword = 'keyword_example' # str | 标题或正文检索关键字。 / Title or content search keyword. (optional)
    status = ['status_example'] # List[str] | 状态过滤条件。 / Status filter. (optional)

    try:
        # 分页查询异步任务 / List asynchronous tasks
        api_response = api_instance.list_conversation_async_tasks(channel_id, conversation_id, current=current, size=size, order_by=order_by, order_direction=order_direction, order_null_handling=order_null_handling, keyword=keyword, status=status)
        print("The response of MessagesApi->list_conversation_async_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->list_conversation_async_tasks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **current** | **int**| 从 0 开始的页码。 / Zero-based page index. | [optional] 
 **size** | **int**| 单页记录数。 / Number of records per page. | [optional] [default to 30]
 **order_by** | [**List[str]**](str.md)| 排序字段列表。 / Ordered list of sort fields. | [optional] 
 **order_direction** | **str**| 排序方向。 / Sort direction. | [optional] [default to &#39;ASC&#39;]
 **order_null_handling** | **str**| 空值排序策略。 / Null ordering strategy. | [optional] [default to &#39;NATIVE&#39;]
 **keyword** | **str**| 标题或正文检索关键字。 / Title or content search keyword. | [optional] 
 **status** | [**List[str]**](str.md)| 状态过滤条件。 / Status filter. | [optional] 

### Return type

[**AsyncTaskPage**](AsyncTaskPage.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 分页查询异步任务 / List asynchronous tasks 的成功响应。 / Successful response for listConversationAsyncTasks. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conversation_messages**
> ConversationMessagePage list_conversation_messages(channel_id, conversation_id, current=current, size=size, order_by=order_by, order_direction=order_direction, order_null_handling=order_null_handling, keyword=keyword)

分页查询会话消息 / List conversation messages

分页查询会话消息 / List conversation messages 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.conversation_message_page import ConversationMessagePage
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
    api_instance = lingya_agents_sdk.MessagesApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    current = 56 # int | 从 0 开始的页码。 / Zero-based page index. (optional)
    size = 30 # int | 单页记录数。 / Number of records per page. (optional) (default to 30)
    order_by = ['order_by_example'] # List[str] | 排序字段列表。 / Ordered list of sort fields. (optional)
    order_direction = 'ASC' # str | 排序方向。 / Sort direction. (optional) (default to 'ASC')
    order_null_handling = 'NATIVE' # str | 空值排序策略。 / Null ordering strategy. (optional) (default to 'NATIVE')
    keyword = 'keyword_example' # str | 标题或正文检索关键字。 / Title or content search keyword. (optional)

    try:
        # 分页查询会话消息 / List conversation messages
        api_response = api_instance.list_conversation_messages(channel_id, conversation_id, current=current, size=size, order_by=order_by, order_direction=order_direction, order_null_handling=order_null_handling, keyword=keyword)
        print("The response of MessagesApi->list_conversation_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->list_conversation_messages: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **current** | **int**| 从 0 开始的页码。 / Zero-based page index. | [optional] 
 **size** | **int**| 单页记录数。 / Number of records per page. | [optional] [default to 30]
 **order_by** | [**List[str]**](str.md)| 排序字段列表。 / Ordered list of sort fields. | [optional] 
 **order_direction** | **str**| 排序方向。 / Sort direction. | [optional] [default to &#39;ASC&#39;]
 **order_null_handling** | **str**| 空值排序策略。 / Null ordering strategy. | [optional] [default to &#39;NATIVE&#39;]
 **keyword** | **str**| 标题或正文检索关键字。 / Title or content search keyword. | [optional] 

### Return type

[**ConversationMessagePage**](ConversationMessagePage.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 分页查询会话消息 / List conversation messages 的成功响应。 / Successful response for listConversationMessages. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

