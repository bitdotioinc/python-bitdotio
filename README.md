# bit.io Python SDK & Command Line Tool

# bitdotio module

Example usage:

```
#!/usr/bin/env python3
import bitdotio
from pprint import pprint

# Connect to bit.io
b = bitdotio.bitdotio(<YOUR_API_KEY>)

pprint(b.list_repos())

# How about some database queries?
conn = b.get_connection()
cur = conn.cursor()
cur.execute("SELECT 1")
pprint(cur.fetchone())
```


## Requirements

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

### Install Postgres

To install Postgres on Windows, go to https://www.postgresql.org/download/ and download the version
that is correct for your computer, or use your operating system's preferred package manager.

After you have Postgres installed you can install this library with `pip install bitdotio[psycopg2]`.


## Usage

Once you have `bitdotio` installed all you need is your API key to start working with bit.io.

You can get your API key by logging into bit.io and scrolling down to the "Connect any data tool" box, clicking on "API/SDK", and copying the key from there.

See https://docs.bit.io/docs/connecting-to-bitio screenshots and examples.


### Python DB-API usage

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


### bitdotio usage

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


# bit.io CLI usage


Installing the bitdotio module also installs the command line tool `bit` which lets you interact with bit.io
from scripts or the command line. This is installed next to your python binary.

You'll want to grab your API key from your bit.io account - to get the key, log into to bit.io and
click on the green "Connect" button, and copy the API key.



```
Usage: bit [OPTIONS] COMMAND [ARGS]...

Options:
  -k, --key TEXT  Your bit.io API key, available when you click the connect
                  button in bit.io  [required]

  -v, --verbose   Verbose output  [default: False]
  --help          Show this message and exit.

Commands:
  import
  query
  repo
```

All of the commands return JSON.

Note that while the examples below use the key on the command line, you can set the key via the enviornment variable
`BITIO_KEY` (this keeps the key from showing up in, eg, a `ps` command, and allows secret injection for systems like Kubernetes):

```
BITIO_KEY=<your key> bit repo list
```

This is the same as:

```
bit -k <your_key> repo list
```

## Importing Data

With the command line tool you can upload data from a file, from a url, or just use JSON directly. All
the importing commands (aside from status) take an optional `table_name` to indicate the destination table name;
if that table doesn't exist the import will create it. If you don't provide a `table_name` bit.io creates a table
based on the filename.


### Importing from a file

```
bit -k <your_key> import file -r my_new_repo -f foo.csv -t from_file
```

You'll get:

```json
{
    "result": "success",
    "message": "Uploaded file addresses.csv saved successfully from sender adam@bit.io and an ingestion job has been created with the status RECEIVED",
    "table_name": "from_file",
    "repo_name": "my_new_repo",
    "job_id": "34a0539f-39f8-483c-84b5-c858c7d26e10",
    "file_name": "addresses.csv"
}
```

You can use that `job_id` in the status command.

You can also pipe your file in; if you do this, you _must_ provide the `table_name` option:

```
cat foo.csv | bit -k <your_key> import file -r my_new_repo -f - --table_name foo_table
```

And you'll get:

```json
{
    "result": "success",
    "message": "Uploaded file <stdin> saved successfully from sender adam@bit.io and an ingestion job has been created with the status RECEIVED",
    "table_name": "foo_table",
    "repo_name": "my_new_repo",
    "job_id": "c9a551b2-3149-4439-9527-952e7a3fe23",
    "file_name": "<stdin>"
}
```

### Import status


```
bit -k <your_key> import status -i 34a0539f-39f8-483c-84b5-c858c7d26e10
```

And you'd get:

```json
{
    "job_id": "34a0539f-39f8-483c-84b5-c858c7d26e10",
    "state": "DONE",
    "status_message": "",
    "retries": 0,
    "file_type": null,
    "original_filename": "addresses.csv",
    "repo_name": "my_new_repo",
    "table_name": "from_file"
}
```


### Import from url
```
bit -k <your_key> import url -r my_new_repo -u https://storage.googleapis.com/bitdotio-demo-datasets/atl_2020_home_sales.csv

```

And you'll get:

```json
{
    "result": "success",
    "message": "https://storage.googleapis.com/bitdotio-demo-datasets/atl_2020_home_sales.csv queued for processing successfully, and an ingestion job has been created with the status RECEIVED",
    "table_name": "atl_2020_home_sales.csv",
    "repo_name": "my_new_repo",
    "job_id": "a837e2ed-2bd2-44ae-a3f0-e18f52274061",
    "file_name": "atl_2020_home_sales.csv",
    "url": "https://storage.googleapis.com/bitdotio-demo-datasets/atl_2020_home_sales.csv"
}
```


### Import JSON

```
echo "[[1,2], [3,4]]" | bit -k <your_key> import json-data -r my_new_repo -t json_test
```

And you'll get:

```json
{
    "result": "success",
    "message": "Uploaded file adam_e6d3aaf4-0469-4bf7-a06a-eb6683c1e563.json saved successfully from sender adam@bit.io and an ingestion job has been created with the status RECEIVED",
    "table_name": "json_test",
    "repo_name": "my_new_repo",
    "job_id": "436d0335-184c-42f1-98b3-d24be2ef7701",
    "file_name": "adam_e6d3aaf4-0469-4bf7-a06a-eb6683c1e563.json"
}
```

## Querying data

You can also query your data with the command line tool:

```
bit -k <your_key> query -q "SELECT *  FROM \"a/demo_repo\".\"atl_home_sales\""
```

Or from stdin:
```
echo  "SELECT *  FROM \"a/demo_repo\".\"atl_home_sales\"" | bit -k <your_key> query -qf -
```

## Repo Management

### List repos

```
bit -k <your_key> repo list
```

You'll get something like:

```json
[
    {
        "name": "demo_repo",
        "description": "",
        "documentation": "",
        "bytes": 622592,
        "is_private": true
    },
    {
        "name": "my_new_repo",
        "description": "",
        "documentation": "",
        "bytes": 13099008,
        "is_private": true
    },
    {
        "name": "my-repo",
        "description": "my-repo",
        "documentation": "",
        "bytes": 16384,
        "is_private": true
    },
    {
        "name": "power-usage",
        "description": "",
        "documentation": "",
        "bytes": 16384,
        "is_private": true
    }
]
```

### Create a repo

```
bit -k <your_key> repo create -r my_new_repo
```

And you'll get:

```json
{
    "name": "my_new_repo",
    "description": "",
    "documentation": "",
    "bytes": 0,
    "is_private": true
}
```

### Get a specific repo's information

```
bit -k <your_key> repo retrieve -r my_new_repo
```

And you'll get:

```json
{
    "name": "my_new_repo",
    "description": "",
    "documentation": "",
    "bytes": 0,
    "is_private": true
}
```
