# lingya_agents_sdk.FilesApi

All URIs are relative to *https://tenant.example.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**confirm_pre_signed_upload**](FilesApi.md#confirm_pre_signed_upload) | **POST** /api/agents/channel/openapi/v1/{channelId}/chat/files/pre-signed-url/confirm | 确认预签名上传 / Confirm a presigned upload
[**create_file_by_content_md5**](FilesApi.md#create_file_by_content_md5) | **POST** /api/agents/channel/openapi/v1/{channelId}/chat/files/contentMd5 | 按 MD5 复用文件 / Reuse a file by MD5
[**create_pre_signed_upload**](FilesApi.md#create_pre_signed_upload) | **POST** /api/agents/channel/openapi/v1/{channelId}/chat/files/pre-signed-url/write | 创建预签名上传地址 / Create a presigned upload URL
[**file_exists_by_content_md5**](FilesApi.md#file_exists_by_content_md5) | **GET** /api/agents/channel/openapi/v1/{channelId}/chat/files/meta/contentMd5 | 检查 MD5 文件是否存在 / Check file existence by MD5
[**get_conversation_file_preview**](FilesApi.md#get_conversation_file_preview) | **GET** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/files/{fileId}/preview | 创建会话文件预览地址 / Create a conversation file preview URL
[**get_plan_intermediate_file_preview**](FilesApi.md#get_plan_intermediate_file_preview) | **GET** /api/agents/channel/openapi/v1/{channelId}/chat/conversations/{conversationId}/messages/{messageId}/plan-intermediate-files/{fileId}/preview | 创建计划快照预览地址 / Create a plan snapshot preview URL


# **confirm_pre_signed_upload**
> AgentFile confirm_pre_signed_upload(channel_id, confirm_upload_input)

确认预签名上传 / Confirm a presigned upload

确认预签名上传 / Confirm a presigned upload 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.agent_file import AgentFile
from lingya_agents_sdk.models.confirm_upload_input import ConfirmUploadInput
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
    api_instance = lingya_agents_sdk.FilesApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    confirm_upload_input = lingya_agents_sdk.ConfirmUploadInput() # ConfirmUploadInput | 确认预签名上传 / Confirm a presigned upload 的 JSON 请求参数。 / JSON request parameters for confirmPreSignedUpload.

    try:
        # 确认预签名上传 / Confirm a presigned upload
        api_response = api_instance.confirm_pre_signed_upload(channel_id, confirm_upload_input)
        print("The response of FilesApi->confirm_pre_signed_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->confirm_pre_signed_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **confirm_upload_input** | [**ConfirmUploadInput**](ConfirmUploadInput.md)| 确认预签名上传 / Confirm a presigned upload 的 JSON 请求参数。 / JSON request parameters for confirmPreSignedUpload. | 

### Return type

[**AgentFile**](AgentFile.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 确认预签名上传 / Confirm a presigned upload 的成功响应。 / Successful response for confirmPreSignedUpload. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_file_by_content_md5**
> AgentFile create_file_by_content_md5(channel_id, create_file_input)

按 MD5 复用文件 / Reuse a file by MD5

按 MD5 复用文件 / Reuse a file by MD5 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.agent_file import AgentFile
from lingya_agents_sdk.models.create_file_input import CreateFileInput
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
    api_instance = lingya_agents_sdk.FilesApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    create_file_input = lingya_agents_sdk.CreateFileInput() # CreateFileInput | 按 MD5 复用文件 / Reuse a file by MD5 的 JSON 请求参数。 / JSON request parameters for createFileByContentMd5.

    try:
        # 按 MD5 复用文件 / Reuse a file by MD5
        api_response = api_instance.create_file_by_content_md5(channel_id, create_file_input)
        print("The response of FilesApi->create_file_by_content_md5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_file_by_content_md5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **create_file_input** | [**CreateFileInput**](CreateFileInput.md)| 按 MD5 复用文件 / Reuse a file by MD5 的 JSON 请求参数。 / JSON request parameters for createFileByContentMd5. | 

### Return type

[**AgentFile**](AgentFile.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 按 MD5 复用文件 / Reuse a file by MD5 的成功响应。 / Successful response for createFileByContentMd5. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_pre_signed_upload**
> GeneratePreSignedUrlOutput create_pre_signed_upload(channel_id, generate_pre_signed_url_input)

创建预签名上传地址 / Create a presigned upload URL

创建预签名上传地址 / Create a presigned upload URL 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.generate_pre_signed_url_input import GeneratePreSignedUrlInput
from lingya_agents_sdk.models.generate_pre_signed_url_output import GeneratePreSignedUrlOutput
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
    api_instance = lingya_agents_sdk.FilesApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    generate_pre_signed_url_input = lingya_agents_sdk.GeneratePreSignedUrlInput() # GeneratePreSignedUrlInput | 创建预签名上传地址 / Create a presigned upload URL 的 JSON 请求参数。 / JSON request parameters for createPreSignedUpload.

    try:
        # 创建预签名上传地址 / Create a presigned upload URL
        api_response = api_instance.create_pre_signed_upload(channel_id, generate_pre_signed_url_input)
        print("The response of FilesApi->create_pre_signed_upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->create_pre_signed_upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **generate_pre_signed_url_input** | [**GeneratePreSignedUrlInput**](GeneratePreSignedUrlInput.md)| 创建预签名上传地址 / Create a presigned upload URL 的 JSON 请求参数。 / JSON request parameters for createPreSignedUpload. | 

### Return type

[**GeneratePreSignedUrlOutput**](GeneratePreSignedUrlOutput.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | 创建预签名上传地址 / Create a presigned upload URL 的成功响应。 / Successful response for createPreSignedUpload. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_exists_by_content_md5**
> FileExists file_exists_by_content_md5(channel_id, content_md5)

检查 MD5 文件是否存在 / Check file existence by MD5

检查 MD5 文件是否存在 / Check file existence by MD5 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.file_exists import FileExists
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
    api_instance = lingya_agents_sdk.FilesApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    content_md5 = 'content_md5_example' # str | 文件内容 MD5。 / MD5 digest of the file content.

    try:
        # 检查 MD5 文件是否存在 / Check file existence by MD5
        api_response = api_instance.file_exists_by_content_md5(channel_id, content_md5)
        print("The response of FilesApi->file_exists_by_content_md5:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->file_exists_by_content_md5: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **content_md5** | **str**| 文件内容 MD5。 / MD5 digest of the file content. | 

### Return type

[**FileExists**](FileExists.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 检查 MD5 文件是否存在 / Check file existence by MD5 的成功响应。 / Successful response for fileExistsByContentMd5. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_conversation_file_preview**
> PreSignedReadUrl get_conversation_file_preview(channel_id, conversation_id, file_id)

创建会话文件预览地址 / Create a conversation file preview URL

创建会话文件预览地址 / Create a conversation file preview URL 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.pre_signed_read_url import PreSignedReadUrl
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
    api_instance = lingya_agents_sdk.FilesApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    file_id = 56 # int | 文件记录 ID。 / File record ID.

    try:
        # 创建会话文件预览地址 / Create a conversation file preview URL
        api_response = api_instance.get_conversation_file_preview(channel_id, conversation_id, file_id)
        print("The response of FilesApi->get_conversation_file_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_conversation_file_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **file_id** | **int**| 文件记录 ID。 / File record ID. | 

### Return type

[**PreSignedReadUrl**](PreSignedReadUrl.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 创建会话文件预览地址 / Create a conversation file preview URL 的成功响应。 / Successful response for getConversationFilePreview. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_plan_intermediate_file_preview**
> PreSignedReadUrl get_plan_intermediate_file_preview(channel_id, conversation_id, message_id, file_id)

创建计划快照预览地址 / Create a plan snapshot preview URL

创建计划快照预览地址 / Create a plan snapshot preview URL 请求会在身份验签和资源归属校验后执行；响应字段以本契约为准。 / The request runs after signature and resource-ownership validation; this contract defines the response fields.

### Example

* Api Key Authentication (OpenApiUser):
* Api Key Authentication (OpenApiAccessKey):
* Api Key Authentication (OpenApiTimestamp):
* Api Key Authentication (OpenApiNonce):
* Api Key Authentication (OpenApiSignature):

```python
import lingya_agents_sdk
from lingya_agents_sdk.models.pre_signed_read_url import PreSignedReadUrl
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
    api_instance = lingya_agents_sdk.FilesApi(api_client)
    channel_id = 'channel_id_example' # str | Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID.
    conversation_id = 'conversation_id_example' # str | 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user.
    message_id = 'message_id_example' # str | 用户消息 ID；必须属于指定会话。 / User-message ID owned by the specified conversation.
    file_id = 56 # int | 文件记录 ID。 / File record ID.

    try:
        # 创建计划快照预览地址 / Create a plan snapshot preview URL
        api_response = api_instance.get_plan_intermediate_file_preview(channel_id, conversation_id, message_id, file_id)
        print("The response of FilesApi->get_plan_intermediate_file_preview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->get_plan_intermediate_file_preview: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **channel_id** | **str**| Agent OpenAPI 渠道 UUID。 / Agent OpenAPI channel UUID. | 
 **conversation_id** | **str**| 会话 ID；必须属于当前外部用户。 / Conversation ID owned by the current external user. | 
 **message_id** | **str**| 用户消息 ID；必须属于指定会话。 / User-message ID owned by the specified conversation. | 
 **file_id** | **int**| 文件记录 ID。 / File record ID. | 

### Return type

[**PreSignedReadUrl**](PreSignedReadUrl.md)

### Authorization

[OpenApiUser](../README.md#OpenApiUser), [OpenApiAccessKey](../README.md#OpenApiAccessKey), [OpenApiTimestamp](../README.md#OpenApiTimestamp), [OpenApiNonce](../README.md#OpenApiNonce), [OpenApiSignature](../README.md#OpenApiSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | 创建计划快照预览地址 / Create a plan snapshot preview URL 的成功响应。 / Successful response for getPlanIntermediateFilePreview. |  -  |
**401** | API error |  -  |
**403** | API error |  -  |
**413** | API error |  -  |
**422** | Validation error |  -  |
**429** | API error |  -  |
**500** | API error |  -  |
**503** | API error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

