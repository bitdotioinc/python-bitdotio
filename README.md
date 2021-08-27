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

```
{'file_name': 'foo.csv',
 'job_id': '34a0539f-39f8-483c-84b5-c858c7d26e10',
 'message': 'Uploaded file foo.csv saved successfully from sender adam@bit.io '
            'and an ingestion job has been created with the status RECEIVED',
 'repo_name': 'my_new_repo',
 'result': 'success',
 'table_name': 'from_file'}
```

You can use that `job_id` in the status command.

You can also pipe your file in; if you do this, you _must_ provide the `table_name` option:

```
cat foo.csv | bit -k <your_key> import file -r my_new_repo -f - --table_name foo_table
```

And you'll get:

```
{'file_name': '<stdin>',
 'job_id': '6b4fad58-ad2a-4506-847c-98a7478f7132',
 'message': 'Uploaded file <stdin> saved successfully from sender adam@bit.io '
            'and an ingestion job has been created with the status RECEIVED',
 'repo_name': 'my_new_repo',
 'result': 'success',
 'table_name': 'foo_table'}
```

### Import status


```
bit -k <your_key> import status -i 34a0539f-39f8-483c-84b5-c858c7d26e10
```

And you'd get:

```
{'file_type': None,
 'job_id': '34a0539f-39f8-483c-84b5-c858c7d26e10',
 'original_filename': 'foo.csv',
 'repo_name': 'my_new_repo',
 'retries': 0,
 'state': 'DONE',
 'status_message': '',
 'table_name': 'from_file'}
```


### Import from url
```
bit -k <your_key> import url -r my_new_repo -u https://storage.googleapis.com/bitdotio-demo-datasets/atl_2020_home_sales.csv

```

And you'll get:

```
{'file_name': 'atl_2020_home_sales.csv',
 'job_id': '3ce55893-0517-4d48-9486-c78319e85b7f',
 'message': 'https://storage.googleapis.com/bitdotio-demo-datasets/atl_2020_home_sales.csv '
            'queued for processing successfully, and an ingestion job has been '
            'created with the status RECEIVED',
 'repo_name': 'my_new_repo',
 'result': 'success',
 'table_name': 'atl_2020_home_sales.csv',
 'url': 'https://storage.googleapis.com/bitdotio-demo-datasets/atl_2020_home_sales.csv'}
```


### Import JSON

```
echo "[[1,2], [3,4]]" | bit -k <your_key> import json-data -r my_new_repo -t json_test
```

And you'll get:

```
{'file_name': 'adam_522adc0b-4b86-4677-aa19-4efe2054925f.json',
 'job_id': '5f43b204-a0ea-41da-b81b-66ba7f01bc93',
 'message': 'Uploaded file adam_522adc0b-4b86-4677-aa19-4efe2054925f.json '
            'saved successfully from sender adam@bit.io and an ingestion job '
            'has been created with the status RECEIVED',
 'repo_name': 'my_new_repo',
 'result': 'success',
 'table_name': 'json_test'}
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
```
[{'bytes': 385024,
 'description': '',
 'documentation': '',
 'is_private': True,
 'name': 'AFL Crowds'}, {'bytes': 0,
 'description': '',
 'documentation': '',
 'is_private': True,
 'name': 'bitio_from_segment'}, {'bytes': 21618688,
 'description': 'FCC data',
 'documentation': '2021 FCC Spectrum Auction information and data.',
 'is_private': False,
 'name': 'FCC'}, {'bytes': 139264,
 'description': 'test for support ticket',
 'documentation': '',
 'is_private': True,
 'name': 'nat_test'}, {'bytes': 0,
 'description': '',
 'documentation': '',
 'is_private': False,
 'name': 'new_repo2'}, {'bytes': 139264,
 'description': 'sadfasdf',
 'documentation': '',
 'is_private': True,
 'name': 'test_nat_2'}]
```

### Create a repo

```
bit -k <your_key> repo create -r my_new_repo
```

And you'll get:

```
{'bytes': 0,
 'description': '',
 'documentation': '',
 'is_private': True,
 'name': 'my_new_repo'}
```

### Get a specific repo's information

```
bit -k <your_key> repo retrieve -r my_new_repo
```

And you'll get:

```
{'bytes': 0,
 'description': '',
 'documentation': '',
 'is_private': True,
 'name': 'my_new_repo'}
```


