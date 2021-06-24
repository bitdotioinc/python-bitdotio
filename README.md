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

# Requirements

In order to support different environments, we have a few ways to install the bitdotio package
with or without the `psycopg2` dependency.

1. If you already have `psycopg2` installed, you can install the default bitdotio package:
```
pip install bitdotio
```

2. If you already have Postgres installed, you can install with the psycopg2 dependency:
```
pip install 'bitdotio[psycopg2]'
```

3. If you do not have or cannot install Postgres, you can install with the psycopg2-binary dependency:
```
pip install 'bitdotio[psycopg2-binary]'
```

## Install Postgres

To install Postgres on Windows, go to https://www.postgresql.org/download/ and download the version
that is correct for your computer, or use your operating system's preferred package manager.

After you have Postgres installed you can install this library with `pip install bitdotio[psycopg2]`.


# Usage

Once you have `bitdotio` installed all you need is your API key to start working with bit.io. 

You can get your API key by logging into bit.io and scrolling down to the "Connect any data tool" box, clicking on "API/SDK", and copying the key from there.

See https://docs.bit.io/docs/connecting-to-bitio screenshots and examples.


## Python DB-API usage

`bitdotio` provides easy Python access to querying your data with just a bit.io API key:

```
#!/usr/bin/env python3
import bitdotio

# Connect to bit.io
b = bitdotio.bitdotio(<YOUR_API_KEY>)

conn = b.get_connection()
cur = conn.cursor()
cur.execute("SELECT 1")
print(cur.fetchone())
```

The connection and cursor provided by `bitdotio` are fully Python DB-API compatible, are in fact Pyscopg2 connections and cursors. 

Full documentation on Psycopg2 can be found on https://www.psycopg.org/docs/usage.html


## bit.io usage

`bitdotio` can also do almost everything you can do on bit.io's main site. 

```
#!/usr/bin/env python3
import bitdotio
from pprint import pprint

# Connect to bit.io
b = bitdotio.bitdotio(<YOUR_API_KEY>)

# Let's see bitdotio's repos
pprint(b.list_repos("bitdotio"))
```

You can use the SDK to create/update/delete repos, tables, columns & endpoints; query data; and share repos. In general the SDK is fully mapped to the REST API; 
the documentation for the REST API is availble at https://docs.bit.io/reference


# bit.io concepts

bit.io is a database, with extra features like easy sharing and collaboration. We have a few concepts that the SDK works with:

* Users - a bit.io user, and data about them. You're limited to what you can see about anyone who isn't you.
* Repostories ("repos") - a schema, in Postgres terms, that contains tables and columns. You can have public and private repositories, and you can write SQL that joins
any repo you have access to with another repo. A repo contains tables, and tables contain columns.
* Sharing - giving access to a repo you own or administer to another bit.io user. You can also use this to invite non-bit.io users to your repo via their email.
* Endpoint - a way to upload data into bit.io. You can create endpoints to allow uploading of data via the SDK, or REST, or HTTPS, or via a uniquely-generated email address. You can
setup your endpoints to expire after a certain date or a certain number of uses. This is very handy for importing your data! Currently, we support XLS, CSV, and JSON file formats.

Detailed documentation on interacting with each concept with the SDK:

 - [Column](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/Column.md)
 - [QConnection](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/QConnection.md)
 - [QEndpoint](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/QEndpoint.md)
 - [QUser](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/QUser.md)
 - [QUserProfile](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/QUserProfile.md)
 - [QueryResult](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/QueryResult.md)
 - [Repo](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/Repo.md)
 - [RepoCollaborators](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/RepoCollaborators.md)
 - [Table](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/Table.md)



# SDK Reference


Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiBitdotio* | [**address_q_connection**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#address_q_connection) | **GET** /users/{user_username}/connections/{name}/address/ | 
*ApiBitdotio* | [**address_q_endpoint**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#address_q_endpoint) | **GET** /users/{user_username}/repos/{repo_name}/endpoints/{name}/address/ | 
*ApiBitdotio* | [**create_column**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#create_column) | **POST** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/ | 
*ApiBitdotio* | [**create_q_connection**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#create_q_connection) | **POST** /users/{user_username}/connections/ | 
*ApiBitdotio* | [**create_q_endpoint**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#create_q_endpoint) | **POST** /users/{user_username}/repos/{repo_name}/endpoints/ | 
*ApiBitdotio* | [**create_query_result**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#create_query_result) | **POST** /query/ | 
*ApiBitdotio* | [**create_repo**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#create_repo) | **POST** /users/{user_username}/repos/ | 
*ApiBitdotio* | [**create_table**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#create_table) | **POST** /users/{user_username}/repos/{repo_name}/tables/ | 
*ApiBitdotio* | [**destroy_column**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#destroy_column) | **DELETE** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
*ApiBitdotio* | [**destroy_q_connection**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#destroy_q_connection) | **DELETE** /users/{user_username}/connections/{name}/ | 
*ApiBitdotio* | [**destroy_q_endpoint**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#destroy_q_endpoint) | **DELETE** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
*ApiBitdotio* | [**destroy_repo**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#destroy_repo) | **DELETE** /users/{user_username}/repos/{name}/ | 
*ApiBitdotio* | [**destroy_table**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#destroy_table) | **DELETE** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 
*ApiBitdotio* | [**list_columns**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#list_columns) | **GET** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/ | 
*ApiBitdotio* | [**list_q_connections**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#list_q_connections) | **GET** /users/{user_username}/connections/ | 
*ApiBitdotio* | [**list_q_endpoints**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#list_q_endpoints) | **GET** /users/{user_username}/repos/{repo_name}/endpoints/ | 
*ApiBitdotio* | [**list_q_users**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#list_q_users) | **GET** /users/ | 
*ApiBitdotio* | [**list_repos**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#list_repos) | **GET** /users/{user_username}/repos/ | 
*ApiBitdotio* | [**list_tables**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#list_tables) | **GET** /users/{user_username}/repos/{repo_name}/tables/ | 
*ApiBitdotio* | [**partial_update_column**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#partial_update_column) | **PATCH** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
*ApiBitdotio* | [**partial_update_q_connection**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#partial_update_q_connection) | **PATCH** /users/{user_username}/connections/{name}/ | 
*ApiBitdotio* | [**partial_update_q_endpoint**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#partial_update_q_endpoint) | **PATCH** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
*ApiBitdotio* | [**partial_update_q_user**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#partial_update_q_user) | **PATCH** /users/{username}/ | 
*ApiBitdotio* | [**partial_update_repo**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#partial_update_repo) | **PATCH** /users/{user_username}/repos/{name}/ | 
*ApiBitdotio* | [**partial_update_table**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#partial_update_table) | **PATCH** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 
*ApiBitdotio* | [**retrieve_column**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#retrieve_column) | **GET** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
*ApiBitdotio* | [**retrieve_q_connection**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#retrieve_q_connection) | **GET** /users/{user_username}/connections/{name}/ | 
*ApiBitdotio* | [**retrieve_q_endpoint**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#retrieve_q_endpoint) | **GET** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
*ApiBitdotio* | [**retrieve_q_user**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#retrieve_q_user) | **GET** /users/{username}/ | 
*ApiBitdotio* | [**retrieve_repo**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#retrieve_repo) | **GET** /users/{user_username}/repos/{name}/ | 
*ApiBitdotio* | [**retrieve_table**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#retrieve_table) | **GET** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 
*ApiBitdotio* | [**share_repo**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#share_repo) | **POST** /users/{user_username}/repos/{name}/share/ | 
*ApiBitdotio* | [**share_table**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#share_table) | **POST** /users/{user_username}/repos/{repo_name}/tables/{current_name}/share/ | 
*ApiBitdotio* | [**update_column**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#update_column) | **PUT** /users/{user_username}/repos/{repo_name}/tables/{table_current_name}/columns/{current_name}/ | 
*ApiBitdotio* | [**update_q_connection**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#update_q_connection) | **PUT** /users/{user_username}/connections/{name}/ | 
*ApiBitdotio* | [**update_q_endpoint**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#update_q_endpoint) | **PUT** /users/{user_username}/repos/{repo_name}/endpoints/{name}/ | 
*ApiBitdotio* | [**update_q_user**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#update_q_user) | **PUT** /users/{username}/ | 
*ApiBitdotio* | [**update_repo**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#update_repo) | **PUT** /users/{user_username}/repos/{name}/ | 
*ApiBitdotio* | [**update_table**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#update_table) | **PUT** /users/{user_username}/repos/{repo_name}/tables/{current_name}/ | 

