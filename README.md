# bit.io Python SDK

Example usage:

```
#!/usr/bin/env python3
import bitdotio
from pprint import pprint

# Connect to bit.io
b = bitdotio.bitdotio(<YOUR_API_KEY>)

# Let's see your repos
pprint(b.list_repos())

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

# Let's see your repos
pprint(b.list_repos())
```

You can use the SDK to create/update/delete repos and query data. In general the SDK is fully mapped to the REST API; 
the documentation for the REST API is availble at https://docs.bit.io/reference


# bit.io concepts

bit.io is a database, with extra features like easy sharing and collaboration. We have a few concepts that the SDK works with:

* Repostories ("repos") - a schema, in Postgres terms, that contains tables and columns. You can have public and private repositories, and you can write SQL that joins
any repo you have access to with another repo. A repo contains tables, and tables contain columns.

Detailed documentation on interacting with each concept with the SDK:

 - [QueryResult](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/QueryResult.md)
 - [Repo](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/Repo.md)



# SDK Reference


Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ApiBitdotio* | [**create_query_result**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#create_query_result) | **POST** /query/ | 
*ApiBitdotio* | [**create_repo**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#create_repo) | **POST** /users/{user_username}/repos/ | 
*ApiBitdotio* | [**destroy_repo**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#destroy_repo) | **DELETE** /users/{user_username}/repos/{name}/ | 
*ApiBitdotio* | [**list_repos**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#list_repos) | **GET** /users/{user_username}/repos/ | 
*ApiBitdotio* | [**partial_update_repo**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#partial_update_repo) | **PATCH** /users/{user_username}/repos/{name}/ | 
*ApiBitdotio* | [**retrieve_repo**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#retrieve_repo) | **GET** /users/{user_username}/repos/{name}/ | 
*ApiBitdotio* | [**update_repo**](https://github.com/bitdotioinc/python-bitdotio/blob/main/docs/ApiBitdotio.md#update_repo) | **PUT** /users/{user_username}/repos/{name}/ | 

