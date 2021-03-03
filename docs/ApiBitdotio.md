# bitdotio.ApiBitdotio

All URIs are relative to *https://api.bit.io/api/v1beta*

Method | HTTP request | Description
------------- | ------------- | -------------
[**address_q_connection**](ApiBitdotio.md#address_q_connection) | **GET** /users/{user_username}/connections/{name}/address/ | 
[**address_q_endpoint**](ApiBitdotio.md#address_q_endpoint) | **GET** /users/{user_username}/repos/{repo_name}/endpoints/{name}/address/ | 
[**create_column**](ApiBitdotio.md#create_column) | **POST** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/ | 
[**create_q_connection**](ApiBitdotio.md#create_q_connection) | **POST** /users/{user_username}/connections/ | 
[**create_q_endpoint**](ApiBitdotio.md#create_q_endpoint) | **POST** /users/{user_username}/repos/{repo_name}/endpoints/ | 
[**create_query_result**](ApiBitdotio.md#create_query_result) | **POST** /query/ | 
[**create_repo**](ApiBitdotio.md#create_repo) | **POST** /users/{user_username}/repos/ | 
[**create_table**](ApiBitdotio.md#create_table) | **POST** /users/{user_username}/repos/{repo_name}/tables/ | 
[**destroy_column**](ApiBitdotio.md#destroy_column) | **DELETE** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
[**destroy_q_connection**](ApiBitdotio.md#destroy_q_connection) | **DELETE** /users/{user_username}/connections/{name}/ | 
[**destroy_q_endpoint**](ApiBitdotio.md#destroy_q_endpoint) | **DELETE** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
[**destroy_repo**](ApiBitdotio.md#destroy_repo) | **DELETE** /users/{user_username}/repos/{name}/ | 
[**destroy_table**](ApiBitdotio.md#destroy_table) | **DELETE** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 
[**list_columns**](ApiBitdotio.md#list_columns) | **GET** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/ | 
[**list_q_connections**](ApiBitdotio.md#list_q_connections) | **GET** /users/{user_username}/connections/ | 
[**list_q_endpoints**](ApiBitdotio.md#list_q_endpoints) | **GET** /users/{user_username}/repos/{repo_name}/endpoints/ | 
[**list_q_users**](ApiBitdotio.md#list_q_users) | **GET** /users/ | 
[**list_repos**](ApiBitdotio.md#list_repos) | **GET** /users/{user_username}/repos/ | 
[**list_tables**](ApiBitdotio.md#list_tables) | **GET** /users/{user_username}/repos/{repo_name}/tables/ | 
[**partial_update_column**](ApiBitdotio.md#partial_update_column) | **PATCH** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
[**partial_update_q_connection**](ApiBitdotio.md#partial_update_q_connection) | **PATCH** /users/{user_username}/connections/{name}/ | 
[**partial_update_q_endpoint**](ApiBitdotio.md#partial_update_q_endpoint) | **PATCH** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
[**partial_update_q_user**](ApiBitdotio.md#partial_update_q_user) | **PATCH** /users/{username}/ | 
[**partial_update_repo**](ApiBitdotio.md#partial_update_repo) | **PATCH** /users/{user_username}/repos/{name}/ | 
[**partial_update_table**](ApiBitdotio.md#partial_update_table) | **PATCH** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 
[**retrieve_column**](ApiBitdotio.md#retrieve_column) | **GET** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
[**retrieve_q_connection**](ApiBitdotio.md#retrieve_q_connection) | **GET** /users/{user_username}/connections/{name}/ | 
[**retrieve_q_endpoint**](ApiBitdotio.md#retrieve_q_endpoint) | **GET** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
[**retrieve_q_user**](ApiBitdotio.md#retrieve_q_user) | **GET** /users/{username}/ | 
[**retrieve_repo**](ApiBitdotio.md#retrieve_repo) | **GET** /users/{user_username}/repos/{name}/ | 
[**retrieve_table**](ApiBitdotio.md#retrieve_table) | **GET** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 
[**share_repo**](ApiBitdotio.md#share_repo) | **POST** /users/{user_username}/repos/{name}/share/ | 
[**share_table**](ApiBitdotio.md#share_table) | **POST** /users/{user_username}/repos/{repo_name}/tables/{current_name}/share/ | 
[**update_column**](ApiBitdotio.md#update_column) | **PUT** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
[**update_q_connection**](ApiBitdotio.md#update_q_connection) | **PUT** /users/{user_username}/connections/{name}/ | 
[**update_q_endpoint**](ApiBitdotio.md#update_q_endpoint) | **PUT** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
[**update_q_user**](ApiBitdotio.md#update_q_user) | **PUT** /users/{username}/ | 
[**update_repo**](ApiBitdotio.md#update_repo) | **PUT** /users/{user_username}/repos/{name}/ | 
[**update_table**](ApiBitdotio.md#update_table) | **PUT** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 


# **address_q_connection**
> QConnection address_q_connection(user_username, name)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.address_q_connection(user_username, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->address_q_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**QConnection**](QConnection.md)

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

# **address_q_endpoint**
> QEndpoint address_q_endpoint(user_username, repo_name, name)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.address_q_endpoint(user_username, repo_name, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->address_q_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**QEndpoint**](QEndpoint.md)

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

# **create_column**
> Column create_column(user_username, repo_name, table_current_name, column=column)



Create a column owned by the authenticated user in the given repo and table. The request body must contain the required fields for the column.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
table_current_name = 'table_current_name_example' # str | 
column = bitdotio.Column() # Column |  (optional)

    try:
        api_response = api_instance.create_column(user_username, repo_name, table_current_name, column=column)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->create_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **table_current_name** | **str**|  | 
 **column** | [**Column**](Column.md)|  | [optional] 

### Return type

[**Column**](Column.md)

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

# **create_q_connection**
> QConnection create_q_connection(user_username, q_connection=q_connection)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
q_connection = bitdotio.QConnection() # QConnection |  (optional)

    try:
        api_response = api_instance.create_q_connection(user_username, q_connection=q_connection)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->create_q_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **q_connection** | [**QConnection**](QConnection.md)|  | [optional] 

### Return type

[**QConnection**](QConnection.md)

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

# **create_q_endpoint**
> QEndpoint create_q_endpoint(user_username, repo_name, q_endpoint=q_endpoint)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
q_endpoint = bitdotio.QEndpoint() # QEndpoint |  (optional)

    try:
        api_response = api_instance.create_q_endpoint(user_username, repo_name, q_endpoint=q_endpoint)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->create_q_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **q_endpoint** | [**QEndpoint**](QEndpoint.md)|  | [optional] 

### Return type

[**QEndpoint**](QEndpoint.md)

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
> QueryResult create_query_result(query_result=query_result)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    query_result = bitdotio.QueryResult() # QueryResult |  (optional)

    try:
        api_response = api_instance.create_query_result(query_result=query_result)
        pprint(api_response)
    except ApiException as e:
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
> Repo create_repo(user_username, repo=repo)



Create a repository owned by the authenticated user. The request body must contain the required fields for the repository.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo = bitdotio.Repo() # Repo |  (optional)

    try:
        api_response = api_instance.create_repo(user_username, repo=repo)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->create_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
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

# **create_table**
> Table create_table(user_username, repo_name, table=table)



Create a table owned by the authenticated user in the given repo. The request body must contain the required fields for the table.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
table = bitdotio.Table() # Table |  (optional)

    try:
        api_response = api_instance.create_table(user_username, repo_name, table=table)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->create_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **table** | [**Table**](Table.md)|  | [optional] 

### Return type

[**Table**](Table.md)

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

# **destroy_column**
> destroy_column(user_username, repo_name, table_current_name, current_name)



Delete the given column.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
table_current_name = 'table_current_name_example' # str | 
current_name = 'current_name_example' # str | 

    try:
        api_instance.destroy_column(user_username, repo_name, table_current_name, current_name)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->destroy_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **table_current_name** | **str**|  | 
 **current_name** | **str**|  | 

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

# **destroy_q_connection**
> destroy_q_connection(user_username, name)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
name = 'name_example' # str | 

    try:
        api_instance.destroy_q_connection(user_username, name)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->destroy_q_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
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

# **destroy_q_endpoint**
> destroy_q_endpoint(user_username, repo_name, name)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
name = 'name_example' # str | 

    try:
        api_instance.destroy_q_endpoint(user_username, repo_name, name)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->destroy_q_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
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

# **destroy_repo**
> destroy_repo(user_username, name)



Delete the given repo.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
name = 'name_example' # str | 

    try:
        api_instance.destroy_repo(user_username, name)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->destroy_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
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

# **destroy_table**
> destroy_table(user_username, repo_name, current_name)



Delete the given table.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
current_name = 'current_name_example' # str | 

    try:
        api_instance.destroy_table(user_username, repo_name, current_name)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->destroy_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **current_name** | **str**|  | 

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

# **list_columns**
> list[Column] list_columns(user_username, repo_name, table_current_name)



Given a username, repo name, and table name, retrieve a list of the table's columns that the user can access in some way.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
table_current_name = 'table_current_name_example' # str | 

    try:
        api_response = api_instance.list_columns(user_username, repo_name, table_current_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->list_columns: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **table_current_name** | **str**|  | 

### Return type

[**list[Column]**](Column.md)

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

# **list_q_connections**
> list[QConnection] list_q_connections(user_username)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 

    try:
        api_response = api_instance.list_q_connections(user_username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->list_q_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 

### Return type

[**list[QConnection]**](QConnection.md)

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

# **list_q_endpoints**
> list[QEndpoint] list_q_endpoints(user_username, repo_name)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 

    try:
        api_response = api_instance.list_q_endpoints(user_username, repo_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->list_q_endpoints: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 

### Return type

[**list[QEndpoint]**](QEndpoint.md)

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

# **list_q_users**
> list[QUser] list_q_users()



API endpoint that allows users to be viewed or edited.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    
    try:
        api_response = api_instance.list_q_users()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->list_q_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QUser]**](QUser.md)

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

# **list_repos**
> list[Repo] list_repos(user_username)



Given a username, retrieve a list of the repositories that the user can access in some way.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 

    try:
        api_response = api_instance.list_repos(user_username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->list_repos: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 

### Return type

[**list[Repo]**](Repo.md)

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

# **list_tables**
> list[Table] list_tables(user_username, repo_name)



Given a username and repo name, retrieve a list of the repository's tables that the user can access in some way.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 

    try:
        api_response = api_instance.list_tables(user_username, repo_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->list_tables: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 

### Return type

[**list[Table]**](Table.md)

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

# **partial_update_column**
> Column partial_update_column(user_username, repo_name, table_current_name, current_name, column=column)



Given a username, repo name, table name, and column name, update one or more fields' value in the given column.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
table_current_name = 'table_current_name_example' # str | 
current_name = 'current_name_example' # str | 
column = bitdotio.Column() # Column |  (optional)

    try:
        api_response = api_instance.partial_update_column(user_username, repo_name, table_current_name, current_name, column=column)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->partial_update_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **table_current_name** | **str**|  | 
 **current_name** | **str**|  | 
 **column** | [**Column**](Column.md)|  | [optional] 

### Return type

[**Column**](Column.md)

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

# **partial_update_q_connection**
> QConnection partial_update_q_connection(user_username, name, q_connection=q_connection)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
name = 'name_example' # str | 
q_connection = bitdotio.QConnection() # QConnection |  (optional)

    try:
        api_response = api_instance.partial_update_q_connection(user_username, name, q_connection=q_connection)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->partial_update_q_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **name** | **str**|  | 
 **q_connection** | [**QConnection**](QConnection.md)|  | [optional] 

### Return type

[**QConnection**](QConnection.md)

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

# **partial_update_q_endpoint**
> QEndpoint partial_update_q_endpoint(user_username, repo_name, name, q_endpoint=q_endpoint)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
name = 'name_example' # str | 
q_endpoint = bitdotio.QEndpoint() # QEndpoint |  (optional)

    try:
        api_response = api_instance.partial_update_q_endpoint(user_username, repo_name, name, q_endpoint=q_endpoint)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->partial_update_q_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **name** | **str**|  | 
 **q_endpoint** | [**QEndpoint**](QEndpoint.md)|  | [optional] 

### Return type

[**QEndpoint**](QEndpoint.md)

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

# **partial_update_q_user**
> QUser partial_update_q_user(username, q_user=q_user)



API endpoint that allows users to be viewed or edited.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    username = 'username_example' # str | 
q_user = bitdotio.QUser() # QUser |  (optional)

    try:
        api_response = api_instance.partial_update_q_user(username, q_user=q_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->partial_update_q_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **q_user** | [**QUser**](QUser.md)|  | [optional] 

### Return type

[**QUser**](QUser.md)

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

# **partial_update_repo**
> Repo partial_update_repo(user_username, name, repo=repo)



Given a username and a repo name, update one or more field's value in the given repo.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
name = 'name_example' # str | 
repo = bitdotio.Repo() # Repo |  (optional)

    try:
        api_response = api_instance.partial_update_repo(user_username, name, repo=repo)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->partial_update_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
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

# **partial_update_table**
> Table partial_update_table(user_username, repo_name, current_name, table=table)



Given a username, repo name, and table name, update one or more fields value in the given table.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
current_name = 'current_name_example' # str | 
table = bitdotio.Table() # Table |  (optional)

    try:
        api_response = api_instance.partial_update_table(user_username, repo_name, current_name, table=table)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->partial_update_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **current_name** | **str**|  | 
 **table** | [**Table**](Table.md)|  | [optional] 

### Return type

[**Table**](Table.md)

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

# **retrieve_column**
> Column retrieve_column(user_username, repo_name, table_current_name, current_name)



Given a username, repo name, table name, and column name, get the given columns's fields and values of those fields.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
table_current_name = 'table_current_name_example' # str | 
current_name = 'current_name_example' # str | 

    try:
        api_response = api_instance.retrieve_column(user_username, repo_name, table_current_name, current_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->retrieve_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **table_current_name** | **str**|  | 
 **current_name** | **str**|  | 

### Return type

[**Column**](Column.md)

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

# **retrieve_q_connection**
> QConnection retrieve_q_connection(user_username, name)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.retrieve_q_connection(user_username, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->retrieve_q_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**QConnection**](QConnection.md)

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

# **retrieve_q_endpoint**
> QEndpoint retrieve_q_endpoint(user_username, repo_name, name)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.retrieve_q_endpoint(user_username, repo_name, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->retrieve_q_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **name** | **str**|  | 

### Return type

[**QEndpoint**](QEndpoint.md)

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

# **retrieve_q_user**
> QUser retrieve_q_user(username)



API endpoint that allows users to be viewed or edited.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    username = 'username_example' # str | 

    try:
        api_response = api_instance.retrieve_q_user(username)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->retrieve_q_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**QUser**](QUser.md)

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
> Repo retrieve_repo(user_username, name)



Given a username and repo name, get the given repo's fields and values of those fields.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
name = 'name_example' # str | 

    try:
        api_response = api_instance.retrieve_repo(user_username, name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->retrieve_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
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

# **retrieve_table**
> Table retrieve_table(user_username, repo_name, current_name)



Given a username, repo name, and table name, get the given table's fields and values of those fields.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
current_name = 'current_name_example' # str | 

    try:
        api_response = api_instance.retrieve_table(user_username, repo_name, current_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->retrieve_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **current_name** | **str**|  | 

### Return type

[**Table**](Table.md)

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

# **share_repo**
> Repo share_repo(user_username, name, repo=repo)



API endpoint that allows repositories to be viewed or edited.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
name = 'name_example' # str | 
repo = bitdotio.Repo() # Repo |  (optional)

    try:
        api_response = api_instance.share_repo(user_username, name, repo=repo)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->share_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
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
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **share_table**
> Table share_table(user_username, repo_name, current_name, table=table)



API endpoint that allows tables to be viewed or edited.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
current_name = 'current_name_example' # str | 
table = bitdotio.Table() # Table |  (optional)

    try:
        api_response = api_instance.share_table(user_username, repo_name, current_name, table=table)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->share_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **current_name** | **str**|  | 
 **table** | [**Table**](Table.md)|  | [optional] 

### Return type

[**Table**](Table.md)

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

# **update_column**
> Column update_column(user_username, repo_name, table_current_name, current_name, column=column)



Given a username, repo name, table name, and column name, update the values of all fields in the given column.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
table_current_name = 'table_current_name_example' # str | 
current_name = 'current_name_example' # str | 
column = bitdotio.Column() # Column |  (optional)

    try:
        api_response = api_instance.update_column(user_username, repo_name, table_current_name, current_name, column=column)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->update_column: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **table_current_name** | **str**|  | 
 **current_name** | **str**|  | 
 **column** | [**Column**](Column.md)|  | [optional] 

### Return type

[**Column**](Column.md)

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

# **update_q_connection**
> QConnection update_q_connection(user_username, name, q_connection=q_connection)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
name = 'name_example' # str | 
q_connection = bitdotio.QConnection() # QConnection |  (optional)

    try:
        api_response = api_instance.update_q_connection(user_username, name, q_connection=q_connection)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->update_q_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **name** | **str**|  | 
 **q_connection** | [**QConnection**](QConnection.md)|  | [optional] 

### Return type

[**QConnection**](QConnection.md)

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

# **update_q_endpoint**
> QEndpoint update_q_endpoint(user_username, repo_name, name, q_endpoint=q_endpoint)



### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
name = 'name_example' # str | 
q_endpoint = bitdotio.QEndpoint() # QEndpoint |  (optional)

    try:
        api_response = api_instance.update_q_endpoint(user_username, repo_name, name, q_endpoint=q_endpoint)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->update_q_endpoint: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **name** | **str**|  | 
 **q_endpoint** | [**QEndpoint**](QEndpoint.md)|  | [optional] 

### Return type

[**QEndpoint**](QEndpoint.md)

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

# **update_q_user**
> QUser update_q_user(username, q_user=q_user)



API endpoint that allows users to be viewed or edited.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    username = 'username_example' # str | 
q_user = bitdotio.QUser() # QUser |  (optional)

    try:
        api_response = api_instance.update_q_user(username, q_user=q_user)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->update_q_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **q_user** | [**QUser**](QUser.md)|  | [optional] 

### Return type

[**QUser**](QUser.md)

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

# **update_repo**
> Repo update_repo(user_username, name, repo=repo)



Given a user and a repo name, update the values of all fields in the given repo.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
name = 'name_example' # str | 
repo = bitdotio.Repo() # Repo |  (optional)

    try:
        api_response = api_instance.update_repo(user_username, name, repo=repo)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->update_repo: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
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

# **update_table**
> Table update_table(user_username, repo_name, current_name, table=table)



Given a username, repo name, and table name, update the values of all fields in the given table.

### Example

* Bearer Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import bitdotio
from bitdotio.rest import ApiException
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
    api_instance = bitdotio.ApiBitdotio(api_client)
    user_username = 'user_username_example' # str | 
repo_name = 'repo_name_example' # str | 
current_name = 'current_name_example' # str | 
table = bitdotio.Table() # Table |  (optional)

    try:
        api_response = api_instance.update_table(user_username, repo_name, current_name, table=table)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ApiBitdotio->update_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_username** | **str**|  | 
 **repo_name** | **str**|  | 
 **current_name** | **str**|  | 
 **table** | [**Table**](Table.md)|  | [optional] 

### Return type

[**Table**](Table.md)

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

