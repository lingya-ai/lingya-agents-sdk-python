# lingya_agents_sdk.SQLApi

All URIs are relative to *https://tenant.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_sql_query_result**](SQLApi.md#export_sql_query_result) | **GET** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/sql-query-results/{resultId}/export | 导出 SQL 结果 / Export SQL results
[**get_sql_query_chart_data**](SQLApi.md#get_sql_query_chart_data) | **GET** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/sql-query-results/{resultId}/chart-data | 读取 SQL 图表数据 / Get SQL chart data
[**get_sql_query_result**](SQLApi.md#get_sql_query_result) | **GET** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/sql-query-results/{resultId} | 分页读取 SQL 结果 / Get paged SQL results


# **export_sql_query_result**
> bytes export_sql_query_result(channel_id, conversation_id, result_id, format, accept=accept)

导出 SQL 结果 / Export SQL results

导出 SQL 结果 / Export SQL results 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

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
    api_instance = lingya_agents_sdk.SQLApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    result_id = 'result_id_example' # str | SQL 查询结果 ID。 / SQL query-result ID.
    format = 'format_example' # str | 导出格式。 / Export format.
    accept = 'accept_example' # str | 期望的导出媒体类型。 / Requested export media type. (optional)

    try:
        # 导出 SQL 结果 / Export SQL results
        api_response = api_instance.export_sql_query_result(channel_id, conversation_id, result_id, format, accept=accept)
        print("The response of SQLApi->export_sql_query_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SQLApi->export_sql_query_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **result_id** | **str**| SQL 查询结果 ID。 / SQL query-result ID. | 
 **format** | **str**| 导出格式。 / Export format. | 
 **accept** | **str**| 期望的导出媒体类型。 / Requested export media type. | [optional] 

### Return type

**bytes**

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Streaming export |  * Content-Disposition -  <br>  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sql_query_chart_data**
> SqlChartDataset get_sql_query_chart_data(channel_id, conversation_id, result_id)

读取 SQL 图表数据 / Get SQL chart data

读取 SQL 图表数据 / Get SQL chart data 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.sql_chart_dataset import SqlChartDataset
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
    api_instance = lingya_agents_sdk.SQLApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    result_id = 'result_id_example' # str | SQL 查询结果 ID。 / SQL query-result ID.

    try:
        # 读取 SQL 图表数据 / Get SQL chart data
        api_response = api_instance.get_sql_query_chart_data(channel_id, conversation_id, result_id)
        print("The response of SQLApi->get_sql_query_chart_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SQLApi->get_sql_query_chart_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **result_id** | **str**| SQL 查询结果 ID。 / SQL query-result ID. | 

### Return type

[**SqlChartDataset**](SqlChartDataset.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 读取 SQL 图表数据 / Get SQL chart data 的成功响应。 / Successful response for getSqlQueryChartData. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sql_query_result**
> SqlQueryResultPage get_sql_query_result(channel_id, conversation_id, result_id, current=current, size=size)

分页读取 SQL 结果 / Get paged SQL results

分页读取 SQL 结果 / Get paged SQL results 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.sql_query_result_page import SqlQueryResultPage
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
    api_instance = lingya_agents_sdk.SQLApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    result_id = 'result_id_example' # str | SQL 查询结果 ID。 / SQL query-result ID.
    current = 0 # int | 从 0 开始的页码。 / Zero-based page index. (optional) (default to 0)
    size = 100 # int | 单页记录数。 / Number of records per page. (optional) (default to 100)

    try:
        # 分页读取 SQL 结果 / Get paged SQL results
        api_response = api_instance.get_sql_query_result(channel_id, conversation_id, result_id, current=current, size=size)
        print("The response of SQLApi->get_sql_query_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SQLApi->get_sql_query_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **result_id** | **str**| SQL 查询结果 ID。 / SQL query-result ID. | 
 **current** | **int**| 从 0 开始的页码。 / Zero-based page index. | [optional] [default to 0]
 **size** | **int**| 单页记录数。 / Number of records per page. | [optional] [default to 100]

### Return type

[**SqlQueryResultPage**](SqlQueryResultPage.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 分页读取 SQL 结果 / Get paged SQL results 的成功响应。 / Successful response for getSqlQueryResult. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

