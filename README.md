# bit.io Python SDK

Example usage:

```
#!/usr/bin/env python3
import bitdotio
from pprint import pprint

# Connect to bit.io
b = bitdotio.bitdotio(<YOUR_API_KEY>)

# Let's see Adam's repos
pprint(b.list_repos("adam"))

# How about some database queries?
conn = b.get_connection()
cur = conn.cursor()
cur.execute("SELECT 1")
pprint(cur.fetchone())
```

## Documentation for API Endpoints

All URIs are relative to *https://api.bit.io/api/v1beta*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiBitdotio* | [**create_import_file**](docs/ApiBitdotio.md#create_import_file) | **POST** /import/file/ | 
*ApiBitdotio* | [**create_import_json**](docs/ApiBitdotio.md#create_import_json) | **POST** /import/json/ | 
*ApiBitdotio* | [**create_import_url**](docs/ApiBitdotio.md#create_import_url) | **POST** /import/url/ | 
*ApiBitdotio* | [**create_query_result**](docs/ApiBitdotio.md#create_query_result) | **POST** /query/ | 
*ApiBitdotio* | [**create_repo**](docs/ApiBitdotio.md#create_repo) | **POST** /repos/ | 
*ApiBitdotio* | [**destroy_repo**](docs/ApiBitdotio.md#destroy_repo) | **DELETE** /repos/{name}/ | 
*ApiBitdotio* | [**list_repos**](docs/ApiBitdotio.md#list_repos) | **GET** /repos/ | 
*ApiBitdotio* | [**partial_update_repo**](docs/ApiBitdotio.md#partial_update_repo) | **PATCH** /repos/{name}/ | 
*ApiBitdotio* | [**retrieve_ingestor_job**](docs/ApiBitdotio.md#retrieve_ingestor_job) | **GET** /import/status/{q_uuid}/ | 
*ApiBitdotio* | [**retrieve_repo**](docs/ApiBitdotio.md#retrieve_repo) | **GET** /repos/{name}/ | 
*ApiBitdotio* | [**update_repo**](docs/ApiBitdotio.md#update_repo) | **PUT** /repos/{name}/ | 


## Documentation For Models

 - [ImportFile](docs/ImportFile.md)
 - [ImportJson](docs/ImportJson.md)
 - [ImportUrl](docs/ImportUrl.md)
 - [IngestorJob](docs/IngestorJob.md)
 - [QueryResult](docs/QueryResult.md)
 - [Repo](docs/Repo.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in bitdotio.apis and bitdotio.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from bitdotio.api.default_api import DefaultApi`
- `from bitdotio.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import bitdotio
from bitdotio.apis import *
from bitdotio.models import *
```

