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
*ApiBitdotio* | [**address_q_connection**](docs/ApiBitdotio.md#address_q_connection) | **GET** /users/{user_username}/connections/{name}/address/ | 
*ApiBitdotio* | [**address_q_endpoint**](docs/ApiBitdotio.md#address_q_endpoint) | **GET** /users/{user_username}/repos/{repo_name}/endpoints/{name}/address/ | 
*ApiBitdotio* | [**create_column**](docs/ApiBitdotio.md#create_column) | **POST** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/ | 
*ApiBitdotio* | [**create_q_connection**](docs/ApiBitdotio.md#create_q_connection) | **POST** /users/{user_username}/connections/ | 
*ApiBitdotio* | [**create_q_endpoint**](docs/ApiBitdotio.md#create_q_endpoint) | **POST** /users/{user_username}/repos/{repo_name}/endpoints/ | 
*ApiBitdotio* | [**create_query_result**](docs/ApiBitdotio.md#create_query_result) | **POST** /query/ | 
*ApiBitdotio* | [**create_repo**](docs/ApiBitdotio.md#create_repo) | **POST** /users/{user_username}/repos/ | 
*ApiBitdotio* | [**create_table**](docs/ApiBitdotio.md#create_table) | **POST** /users/{user_username}/repos/{repo_name}/tables/ | 
*ApiBitdotio* | [**destroy_column**](docs/ApiBitdotio.md#destroy_column) | **DELETE** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
*ApiBitdotio* | [**destroy_q_connection**](docs/ApiBitdotio.md#destroy_q_connection) | **DELETE** /users/{user_username}/connections/{name}/ | 
*ApiBitdotio* | [**destroy_q_endpoint**](docs/ApiBitdotio.md#destroy_q_endpoint) | **DELETE** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
*ApiBitdotio* | [**destroy_repo**](docs/ApiBitdotio.md#destroy_repo) | **DELETE** /users/{user_username}/repos/{name}/ | 
*ApiBitdotio* | [**destroy_table**](docs/ApiBitdotio.md#destroy_table) | **DELETE** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 
*ApiBitdotio* | [**list_columns**](docs/ApiBitdotio.md#list_columns) | **GET** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/ | 
*ApiBitdotio* | [**list_q_connections**](docs/ApiBitdotio.md#list_q_connections) | **GET** /users/{user_username}/connections/ | 
*ApiBitdotio* | [**list_q_endpoints**](docs/ApiBitdotio.md#list_q_endpoints) | **GET** /users/{user_username}/repos/{repo_name}/endpoints/ | 
*ApiBitdotio* | [**list_q_users**](docs/ApiBitdotio.md#list_q_users) | **GET** /users/ | 
*ApiBitdotio* | [**list_repos**](docs/ApiBitdotio.md#list_repos) | **GET** /users/{user_username}/repos/ | 
*ApiBitdotio* | [**list_tables**](docs/ApiBitdotio.md#list_tables) | **GET** /users/{user_username}/repos/{repo_name}/tables/ | 
*ApiBitdotio* | [**partial_update_column**](docs/ApiBitdotio.md#partial_update_column) | **PATCH** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
*ApiBitdotio* | [**partial_update_q_connection**](docs/ApiBitdotio.md#partial_update_q_connection) | **PATCH** /users/{user_username}/connections/{name}/ | 
*ApiBitdotio* | [**partial_update_q_endpoint**](docs/ApiBitdotio.md#partial_update_q_endpoint) | **PATCH** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
*ApiBitdotio* | [**partial_update_q_user**](docs/ApiBitdotio.md#partial_update_q_user) | **PATCH** /users/{username}/ | 
*ApiBitdotio* | [**partial_update_repo**](docs/ApiBitdotio.md#partial_update_repo) | **PATCH** /users/{user_username}/repos/{name}/ | 
*ApiBitdotio* | [**partial_update_table**](docs/ApiBitdotio.md#partial_update_table) | **PATCH** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 
*ApiBitdotio* | [**retrieve_column**](docs/ApiBitdotio.md#retrieve_column) | **GET** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
*ApiBitdotio* | [**retrieve_q_connection**](docs/ApiBitdotio.md#retrieve_q_connection) | **GET** /users/{user_username}/connections/{name}/ | 
*ApiBitdotio* | [**retrieve_q_endpoint**](docs/ApiBitdotio.md#retrieve_q_endpoint) | **GET** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
*ApiBitdotio* | [**retrieve_q_user**](docs/ApiBitdotio.md#retrieve_q_user) | **GET** /users/{username}/ | 
*ApiBitdotio* | [**retrieve_repo**](docs/ApiBitdotio.md#retrieve_repo) | **GET** /users/{user_username}/repos/{name}/ | 
*ApiBitdotio* | [**retrieve_table**](docs/ApiBitdotio.md#retrieve_table) | **GET** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 
*ApiBitdotio* | [**share_repo**](docs/ApiBitdotio.md#share_repo) | **POST** /users/{user_username}/repos/{name}/share/ | 
*ApiBitdotio* | [**share_table**](docs/ApiBitdotio.md#share_table) | **POST** /users/{user_username}/repos/{repo_name}/tables/{current_name}/share/ | 
*ApiBitdotio* | [**update_column**](docs/ApiBitdotio.md#update_column) | **PUT** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
*ApiBitdotio* | [**update_q_connection**](docs/ApiBitdotio.md#update_q_connection) | **PUT** /users/{user_username}/connections/{name}/ | 
*ApiBitdotio* | [**update_q_endpoint**](docs/ApiBitdotio.md#update_q_endpoint) | **PUT** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
*ApiBitdotio* | [**update_q_user**](docs/ApiBitdotio.md#update_q_user) | **PUT** /users/{username}/ | 
*ApiBitdotio* | [**update_repo**](docs/ApiBitdotio.md#update_repo) | **PUT** /users/{user_username}/repos/{name}/ | 
*ApiBitdotio* | [**update_table**](docs/ApiBitdotio.md#update_table) | **PUT** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 


## Documentation For Models

 - [Column](docs/Column.md)
 - [QConnection](docs/QConnection.md)
 - [QEndpoint](docs/QEndpoint.md)
 - [QUser](docs/QUser.md)
 - [QUserProfile](docs/QUserProfile.md)
 - [QueryResult](docs/QueryResult.md)
 - [Repo](docs/Repo.md)
 - [RepoCollaborators](docs/RepoCollaborators.md)
 - [Table](docs/Table.md)


## Documentation For Authorization


## bearerAuth

- **Type**: Bearer authentication


## Author




