# bit.io Python SDK & Command Line Tool

# bitdotio module

The v2 SDK currently only supports generation of pre-configured `psycopg2` connections
to v2 bit.io. We plan to add further SDK operations as we begin expanding the 
bit.io [Developer API](https://docs.bit.io/reference/get_db_list_v2beta_db__get). 

Example v2 usage:
```python
#!/usr/bin/env python3
import bitdotio
from pprint import pprint

# Instantiate a bit.io client for connecting to databases
b = bitdotio.bitdotio(<YOUR_API_KEY>)

# Connect to a database by name 
conn = b.get_connection(<YOUR_DATABASE_NAME>)
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

You can get your API key by logging into bit.io and opening [the "Connect" tab](https://docs.bit.io/docs/your-connection-credentials) on a database page.


### Python DB-API usage

`bitdotio` provides easy Python access to querying your data with just a bit.io API key:

```python
#!/usr/bin/env python3
import bitdotio

# Connect to bit.io
b = bitdotio.bitdotio(<YOUR_API_KEY>)

conn = b.get_connection(<YOUR_DATABASE_NAME>)
cur = conn.cursor()
cur.execute("SELECT 1")
print(cur.fetchone())
```

The connection and cursor provided by `bitdotio` are fully Python DB-API compatible, are in fact Pyscopg2 connections and cursors.

Full documentation on Psycopg2 can be found on https://www.psycopg.org/docs/usage.html.