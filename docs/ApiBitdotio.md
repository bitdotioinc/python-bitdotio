# bitdotio.ApiBitdotio

All URIs are relative to *https://api.bit.io/api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_import_file**](ApiBitdotio.md#create_import_file) | **POST** /import/file/ | 
[**create_import_json**](ApiBitdotio.md#create_import_json) | **POST** /import/json/ | 
[**create_import_url**](ApiBitdotio.md#create_import_url) | **POST** /import/url/ | 
[**create_query_result**](ApiBitdotio.md#create_query_result) | **POST** /query/ | 
[**create_repo**](ApiBitdotio.md#create_repo) | **POST** /repos/ | 
[**destroy_repo**](ApiBitdotio.md#destroy_repo) | **DELETE** /repos/{name}/ | 
[**list_repos**](ApiBitdotio.md#list_repos) | **GET** /repos/ | 
[**partial_update_repo**](ApiBitdotio.md#partial_update_repo) | **PATCH** /repos/{name}/ | 
[**retrieve_ingestor_job**](ApiBitdotio.md#retrieve_ingestor_job) | **GET** /import/status/{q_uuid}/ | 
[**retrieve_repo**](ApiBitdotio.md#retrieve_repo) | **GET** /repos/{name}/ | 
[**update_repo**](ApiBitdotio.md#update_repo) | **PUT** /repos/{name}/ | 


# **create_import_file**
> ImportFile create_import_file()



### Example

* Bearer Authentication (bearerAuth):
```python
import time
import bitdotio
from bitdotio.api import api_bitdotio
from bitdotio.model.import_file import ImportFile
from pprint import pprint
# Defining the host is optional and defaults to https://api.bit.io/api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = bitdotio.Configuration(
    host = "https://api.bit.io/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = bitdotio.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with bitdotio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_bitdotio.ApiBitdotio(api_client)
    import_file = ImportFile(
        file_to_import=open('/path/to/file', 'rb'),
        table_name="table_name_example",
        create_table_if_not_exists=True,
        repo_name="repo_name_example",
    ) # ImportFile |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_import_file(import_file=import_file)
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->create_import_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_file** | [**ImportFile**](ImportFile.md)|  | [optional]

### Return type

[**ImportFile**](ImportFile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_import_json**
> ImportJson create_import_json()



### Example

* Bearer Authentication (bearerAuth):
```python
import time
import bitdotio
from bitdotio.api import api_bitdotio
from bitdotio.model.import_json import ImportJson
from pprint import pprint
# Defining the host is optional and defaults to https://api.bit.io/api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = bitdotio.Configuration(
    host = "https://api.bit.io/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = bitdotio.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with bitdotio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_bitdotio.ApiBitdotio(api_client)
    import_json = ImportJson(
        data={},
        table_name="table_name_example",
        repo_name="repo_name_example",
        create_table_if_not_exists=True,
    ) # ImportJson |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_import_json(import_json=import_json)
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->create_import_json: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_json** | [**ImportJson**](ImportJson.md)|  | [optional]

### Return type

[**ImportJson**](ImportJson.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_import_url**
> ImportUrl create_import_url()



### Example

* Bearer Authentication (bearerAuth):
```python
import time
import bitdotio
from bitdotio.api import api_bitdotio
from bitdotio.model.import_url import ImportUrl
from pprint import pprint
# Defining the host is optional and defaults to https://api.bit.io/api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = bitdotio.Configuration(
    host = "https://api.bit.io/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = bitdotio.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with bitdotio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_bitdotio.ApiBitdotio(api_client)
    import_url = ImportUrl(
        url="url_example",
        table_name="table_name_example",
        repo_name="repo_name_example",
        create_table_if_not_exists=True,
    ) # ImportUrl |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_import_url(import_url=import_url)
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->create_import_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **import_url** | [**ImportUrl**](ImportUrl.md)|  | [optional]

### Return type

[**ImportUrl**](ImportUrl.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_query_result**
> QueryResult create_query_result()



### Example

* Bearer Authentication (bearerAuth):
```python
import time
import bitdotio
from bitdotio.api import api_bitdotio
from bitdotio.model.query_result import QueryResult
from pprint import pprint
# Defining the host is optional and defaults to https://api.bit.io/api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = bitdotio.Configuration(
    host = "https://api.bit.io/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = bitdotio.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with bitdotio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_bitdotio.ApiBitdotio(api_client)
    query_result = QueryResult(
        query_string="query_string_example",
        fields={},
        data=[
            {},
        ],
    ) # QueryResult |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_query_result(query_result=query_result)
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->create_query_result: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_result** | [**QueryResult**](QueryResult.md)|  | [optional]

### Return type

[**QueryResult**](QueryResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_repo**
> Repo create_repo()



Create a repository owned by the authenticated user. The request body must contain the required fields for the repository.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import bitdotio
from bitdotio.api import api_bitdotio
from bitdotio.model.repo import Repo
from pprint import pprint
# Defining the host is optional and defaults to https://api.bit.io/api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = bitdotio.Configuration(
    host = "https://api.bit.io/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = bitdotio.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with bitdotio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_bitdotio.ApiBitdotio(api_client)
    repo = Repo(
        name="name_example",
        description="description_example",
        documentation="documentation_example",
        license="license_example",
        is_private=True,
    ) # Repo |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_repo(repo=repo)
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->create_repo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repo** | [**Repo**](Repo.md)|  | [optional]

### Return type

[**Repo**](Repo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **destroy_repo**
> destroy_repo(name)



Delete the given repo.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import bitdotio
from bitdotio.api import api_bitdotio
from pprint import pprint
# Defining the host is optional and defaults to https://api.bit.io/api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = bitdotio.Configuration(
    host = "https://api.bit.io/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = bitdotio.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with bitdotio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_bitdotio.ApiBitdotio(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.destroy_repo(name)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->destroy_repo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_repos**
> [Repo] list_repos()



Retrieve a list of the repositories that the currently logged-in user can access in some way.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import bitdotio
from bitdotio.api import api_bitdotio
from bitdotio.model.repo import Repo
from pprint import pprint
# Defining the host is optional and defaults to https://api.bit.io/api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = bitdotio.Configuration(
    host = "https://api.bit.io/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = bitdotio.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with bitdotio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_bitdotio.ApiBitdotio(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        api_response = api_instance.list_repos()
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->list_repos: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Repo]**](Repo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update_repo**
> Repo partial_update_repo(name)



Given a repo name, update one or more field's value in the given repo.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import bitdotio
from bitdotio.api import api_bitdotio
from bitdotio.model.repo import Repo
from pprint import pprint
# Defining the host is optional and defaults to https://api.bit.io/api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = bitdotio.Configuration(
    host = "https://api.bit.io/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = bitdotio.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with bitdotio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_bitdotio.ApiBitdotio(api_client)
    name = "name_example" # str | 
    repo = Repo(
        name="name_example",
        description="description_example",
        documentation="documentation_example",
        license="license_example",
        is_private=True,
    ) # Repo |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.partial_update_repo(name)
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->partial_update_repo: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.partial_update_repo(name, repo=repo)
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->partial_update_repo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **repo** | [**Repo**](Repo.md)|  | [optional]

### Return type

[**Repo**](Repo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_ingestor_job**
> IngestorJob retrieve_ingestor_job(q_uuid)



### Example

* Bearer Authentication (bearerAuth):
```python
import time
import bitdotio
from bitdotio.api import api_bitdotio
from bitdotio.model.ingestor_job import IngestorJob
from pprint import pprint
# Defining the host is optional and defaults to https://api.bit.io/api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = bitdotio.Configuration(
    host = "https://api.bit.io/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = bitdotio.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with bitdotio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_bitdotio.ApiBitdotio(api_client)
    q_uuid = "q_uuid_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_ingestor_job(q_uuid)
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->retrieve_ingestor_job: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q_uuid** | **str**|  |

### Return type

[**IngestorJob**](IngestorJob.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_repo**
> Repo retrieve_repo(name)



Given a repo name, get the given repo's fields and values of those fields.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import bitdotio
from bitdotio.api import api_bitdotio
from bitdotio.model.repo import Repo
from pprint import pprint
# Defining the host is optional and defaults to https://api.bit.io/api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = bitdotio.Configuration(
    host = "https://api.bit.io/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = bitdotio.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with bitdotio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_bitdotio.ApiBitdotio(api_client)
    name = "name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.retrieve_repo(name)
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->retrieve_repo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |

### Return type

[**Repo**](Repo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_repo**
> Repo update_repo(name)



Given a repo name, update the values of all fields in the given repo.

### Example

* Bearer Authentication (bearerAuth):
```python
import time
import bitdotio
from bitdotio.api import api_bitdotio
from bitdotio.model.repo import Repo
from pprint import pprint
# Defining the host is optional and defaults to https://api.bit.io/api/v1beta
# See configuration.py for a list of all supported configuration parameters.
configuration = bitdotio.Configuration(
    host = "https://api.bit.io/api/v1beta"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = bitdotio.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with bitdotio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_bitdotio.ApiBitdotio(api_client)
    name = "name_example" # str | 
    repo = Repo(
        name="name_example",
        description="description_example",
        documentation="documentation_example",
        license="license_example",
        is_private=True,
    ) # Repo |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_repo(name)
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->update_repo: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_repo(name, repo=repo)
        pprint(api_response)
    except bitdotio.ApiException as e:
        print("Exception when calling ApiBitdotio->update_repo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  |
 **repo** | [**Repo**](Repo.md)|  | [optional]

### Return type

[**Repo**](Repo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

