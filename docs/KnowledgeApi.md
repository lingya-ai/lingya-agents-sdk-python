# lingya_agents_sdk.KnowledgeApi

All URIs are relative to *https://tenant.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_citation_metadata**](KnowledgeApi.md#get_citation_metadata) | **GET** /api/agents/channel/openapi/v1/{channelId}/chat/knowledge-bases/citations/{citationType}/{referenceId}/metadata | 读取引用元数据 / Get citation metadata
[**get_citation_metadata_batch**](KnowledgeApi.md#get_citation_metadata_batch) | **POST** /api/agents/channel/openapi/v1/{channelId}/chat/knowledge-bases/citations/metadata | 批量读取引用元数据 / Get citation metadata in batch


# **get_citation_metadata**
> CitationMetadata get_citation_metadata(channel_id, citation_type, reference_id)

读取引用元数据 / Get citation metadata

读取引用元数据 / Get citation metadata 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.citation_metadata import CitationMetadata
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
    api_instance = lingya_agents_sdk.KnowledgeApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    citation_type = 'citation_type_example' # str | 知识引用类型。 / Knowledge citation type.
    reference_id = 56 # int | 知识引用记录 ID。 / Knowledge-reference record ID.

    try:
        # 读取引用元数据 / Get citation metadata
        api_response = api_instance.get_citation_metadata(channel_id, citation_type, reference_id)
        print("The response of KnowledgeApi->get_citation_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->get_citation_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **citation_type** | **str**| 知识引用类型。 / Knowledge citation type. | 
 **reference_id** | **int**| 知识引用记录 ID。 / Knowledge-reference record ID. | 

### Return type

[**CitationMetadata**](CitationMetadata.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 读取引用元数据 / Get citation metadata 的成功响应。 / Successful response for getCitationMetadata. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_citation_metadata_batch**
> CitationMetadataList get_citation_metadata_batch(channel_id, returned_reference)

批量读取引用元数据 / Get citation metadata in batch

批量读取引用元数据 / Get citation metadata in batch 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.citation_metadata_list import CitationMetadataList
from lingya_agents_sdk.models.returned_reference import ReturnedReference
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
    api_instance = lingya_agents_sdk.KnowledgeApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    returned_reference = [lingya_agents_sdk.ReturnedReference()] # List[ReturnedReference] | 批量读取引用元数据 / Get citation metadata in batch 的 JSON 请求参数。 / JSON request parameters for getCitationMetadataBatch.

    try:
        # 批量读取引用元数据 / Get citation metadata in batch
        api_response = api_instance.get_citation_metadata_batch(channel_id, returned_reference)
        print("The response of KnowledgeApi->get_citation_metadata_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeApi->get_citation_metadata_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **returned_reference** | [**List[ReturnedReference]**](ReturnedReference.md)| 批量读取引用元数据 / Get citation metadata in batch 的 JSON 请求参数。 / JSON request parameters for getCitationMetadataBatch. | 

### Return type

[**CitationMetadataList**](CitationMetadataList.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 批量读取引用元数据 / Get citation metadata in batch 的成功响应。 / Successful response for getCitationMetadataBatch. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

