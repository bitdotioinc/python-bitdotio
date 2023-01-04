# bit.io Python SDK & Command Line Tool

## Installation

In order to support different environments, we have a few ways to install the bitdotio
package with or without the `psycopg2` dependency.

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

## Versioning

`python-bitdotio` uses [semantic versioning](https://semver.org/).

# `bitdotio` module

## Usage

The `bitdotio` module consists of a `bitdotio` SDK object which provides helpful
utilities for creating and managing pre-configured connections to bit.io databases
via `psycopg2`, as well as easy methods for accessing the functionality exposed by the
[bit.io developer API](https://docs.bit.io/reference)

Once you have `bitdotio` installed all you need is your API key to start working with bit.io.

You can get your API key by logging into bit.io and opening [the "Connect" tab](https://docs.bit.io/docs/your-connection-credentials) on a database page.

### Example usage

See API reference at the bottom of this document for a full list of methods provided by
the SDK.

```python
import os
import time

from bitdotio import bitdotio


# Load bit.io API key from environment variable
BITIO_KEY = os.environ.get("BITIO_KEY")

# Instantiate the bit.io SDK object
b = bitdotio(BITIO_KEY)

# Create a new public database on bit.io
db_metadata = b.create_database("my-db", is_private=False)
db_name = db_metadata["name"]

# Use a pooled cursor to insert some data
with b.pooled_cursor(db_name) as cur:
    cur.execute("CREATE TABLE person (name text, age integer);")
    people = [("Alice", 45), ("Bob", 84), ("Catherine", 19), ("Davis", 22), ("Emily", 34)]
    for name, age in people:
        cur.execute("INSERT INTO person (name, age) VALUES (%s, %s)", (name, age))

# Execute a query via the HTTP API
print(b.query(db_name, "SELECT * FROM person", data_format="objects"))

# Create a new table "city" by importing a file.
with open("city.csv", "rb") as f:
    job_status = b.create_import_job("my-username/my-db", "city", file=f)
    # Poll the status of the job until done
    while True:
        job_status = b.get_import_job(job_status["id"])
        if job_status["state"] == "DONE":
            break
        if job_status["state"] == "FAILED":
            # If the import failed for whatever reason, raise an exception with the
            # error info.
            error_id = job_status["error_id"]
            error_type = job_status["error_type"]
            error_details = job_status["error_details"]
            raise Exception(
                f"Import failed. error_id={error_id} error_type={error_type}, error_details={error_details}"
            )

        # Wait a little before trying again
        time.sleep(0.2)
```

### Making queries

#### Connecting directly

The `bitdotio` SDK object provides the methods `pooled_connection`, `pooled_cursor`, and
`get_connection` for connecting directly to your database (see below for discusson on
when to use each of these). The connections/cursors returned by these methods are
`psycopg2` connections and cursors, which are fully compatible with the
[Python DB-API](https://peps.python.org/pep-0249/). Full documentation on `psycopg2` can
be found [here](https://www.psycopg.org/docs/usage.html.).

It is preferable to use direct connections in the majority of cases, since they have
superior performance and enable more features compared to the `query` method. In
particular we strongly recommend using direct connections in programs that are
long-running, require transaction management, or transfer large quantities of data.

#### The `query` method

The `query` runs queries via the bit.io HTTP API, and therefore will have worse
performance and feature support than direct connections. Importantly, each query run
via the `query` method is run in a single transaction. The `query` method is recommended
in situations where installing a database driver is undesirable or impossible, when
queries are being run very infrequently, or in very short-lived contexts such as one-off
scripts or serverless backends.

### Connection pooling and management

The recommended way to obtain a direct connection to a bit.io database is via a
connection pool. In order to support scaling to zero, bit.io automatically closes idle
connections after a period of time, and puts databases into a dormant state when there
are no live connections. If you are designing a long-running application, you should
make sure that your database access pattern is resilient to connection closures and
database shutdowns. The best way to do this is via a connection pool. Acquiring
connections from a connection pool allows connection re-use, and handles reconnects in
the event that a connection is dropped. The `bitdotio` SDK object internally manages a
thread-safe connection pool per-database that the caller connects to, and provides two
helpful context mangers for acquiring connections from a pool:
- `pooled_connection`: A context manager providing a `psycopg2` connection to the
  given database acquired from a connection pool. When exiting the context created by
  this context manager, the connection is returned to the pool if still open, or
  discarded if closed. It is recommended to use this method when executing multiple
  transacions, or in situations where explicit transaction management is required.
- `pooled_cursor`: A context manager providing a `psycopg2` cursor created from a
  connection acquired from a connection pool. When exiting the context created by this
  context manager, the cursor's tansaction will be committed, and its connection will be
  returned to the connection pool. It is recommended to use this method in situations
  where a single transaction is required without any complex handling logic. For
  example, performing a sequence of `SELECT` queries, or performing a single insertion
  or update.

There may be situations in which a self-managed, unpooled connection is needed. For
example, if the client needs to persist state onto the connection's database session using
the `SET` command. For such situations, the SDK object provides the `get_connection`
method.

For more information on all of the above, refer to the `psycopg2` documentation on
[connections](https://www.psycopg.org/docs/connection.html),
[cursors](https://www.psycopg.org/docs/cursor.html),
and [pools](https://www.psycopg.org/docs/pool.html).

### Data imports and exports

The `bitdotio` SDK object provides helper methods to facilitate importing and exporting
data from your bit.io database.

To import data into a table on your bit.io database from a file locally or on the web
you can use the `create_import_job` method. To export data from a query or a table in
your bit.io database you can use the `create_export_job` method.

These methods have somewhat symmetrical workflows in that they both kick off jobs on
the bit.io backend which execute asynchronously, and have companion methods
(`get_import_job`, and `get_export_job`) to check on the status of a running job.

At a high level, the procedure for doing a data import looks like:
1. Call `create_import_job` and get back the job status
2. Use the job status info to poll `get_import_job` until the job status is reported
   as `DONE` or `FAILED`
3. If `DONE`, the data has been successfully imported and your table is ready to query
4. If `FAILED`, the job status object will contain metadata describing what went wrong.

Similarly, a data export looks like:
1. Call `create_export_job` and get back the job status
2. Use the job status info to poll `get_export_job` until the job status is reported
   as `DONE` or `FAILED`
3. If `DONE`, the exported data will be available to download at the `download_url`
   included in the job status info.
4. If `FAILED`, the job status object will contain metadata describing what went wrong.

### Multiprocessing

The `bitdotio` SDK object is not safe to share between multiple processes. If you are
programming in a multiprocess environment, ensure that a `bitdotio` SDK object is
created per-process, not pre-fork.

# `bit` CLI

Installing the `bitdotio` module also installs the command line tool `bit` which lets
you interact with bit.io from scripts or the command line. This is installed next to
your python binary.

You'll want to grab your API key from your bit.io account - to get the key, log into to
bit.io, go to any database, and retrieve it from the "Connect" tab.

```
Usage: bit [OPTIONS] COMMAND [ARGS]...

Options:
  -k, --key TEXT  Your bit.io API key, available when you click the connect
                  button in bit.io
  --help          Show this message and exit.

Commands:
  db
  query
```

All of the commands return JSON.

You can supply your API key either via the `-k/--key` argument, or by setting the it to
the `BITIO_KEY` environment variable. The latter option keeps the key from showing up
in, eg, a `ps` command, and allows secret injection for systems like Kubernetes.


### Examples

#### List databases
```sh
BITIO_KEY=<your key> bit db list
```

This is the same as:

```sh
bit -k <your-key> db list
```

#### Run a query
```sh
bit -k <your-key> query -d "username/dbname" -q "SELECT * FROM my_table"
```

# API Reference

#### `bitdotio(access_token, min_conn=0, max_conn=100)`

Returns an instance of the bit.io SDK object.

_Args_:
- `access_token (str)`: Your bit.io API key

_Kwargs_:
- `min_conn (int)`: The minimum number of live connections per database connection pool.
- `max_conn (int)`: The maximum number of live connections per database connection pool.

_Returns_:

A bit.io SDK instance

<hr>

#### `bitdotio.pooled_connection(db_name)`

Creates a context manager which provides a connection from the connection pool for the
given database name. When the context manager is exited, the connection's transaction
will be committed, and the connection will be returned to the connection pool.

_Args_:
- `db_name (str)`: The name of the database to connect to.

_Returns_:

Context manager yielding a `psycopg2.connection`.

<hr>

#### `bitdotio.pooled_cursor(db_name)`

Creates a context manager which provides a cursor from the connection pool for the
given database name. When the context manager is exited, the cursor's transaction will
be committed, and its connection will be returned to the connection pool.

_Args_:
- `db_name (str)`: The name of the database to connect to.

_Returns_:

Context manager yielding a `psycopg2.connection`.

<hr>

#### `bitdotio.get_connection(db_name)`

Returns an unmanaged, unpooled connection to the given database.

_Args_:
- `db_name (str)`: The name of the database to connect to.

_Returns_:

A `psycopg2.connection` object configured for the given database.

<hr>

#### `bitdotio.query(db_name, query_str, data_format=None)`

Execute a query via the bit.io HTTP API

_Args_:
- `db_name (str)`: Name of the database to execute a query against.
- `query_str (str)`: Query to execute.

_Kwargs_:
- `data_format (Optional[str])`:

_Returns_:

Dictionary describing query results.

<hr>

#### `bitdotio.list_databases()`

List metadata pertaining to databases the requester is an owner or collaborator of.

_Returns_:

List of dictionaries describing database metadata.

<hr>

#### `bitdotio.create_database(name, is_private=True, storage_limit_bytes=None)`

_Args_:
- `name (str)`: Name of the database being created (excluding the owner's username)

_Kwargs_:
- `is_private (bool)`: Whether or not the database is set to private. Databases default
  to private.
- `storage_limit_bytes (Optional[int])`: Maximum storage for the database in bytes.
  Limits and defaults are enforced based on billing plan regardless of what is set here.

_Returns_:

Dict containing metadata about the newly created database.

<hr>

#### `bitdotio.get_database(db_name)`

Get metadata about a single database.

_Args_:
- `db_name (str)`: Name of the database to fetch metadata for.

_Returns_:

Dict containing metadata about the given database.

<hr>

#### `bitdotio.update_database(db_name, name=None, is_private=None, storage_limit_bytes=None)`

Update metadata parameters for a given database.

_Args_:
- `db_name (str)`: Name of the database to update.

_Kwargs_:
- `name (Optional[str])`: New name for the database (excluding the owner's username).
- `is_private (Optional[str])`: Whether or not the database is set to private.
- `storage_limit_bytes (Optional[int])`: Maximum storage for the database in bytes.
  Limits and defaults are enforced based on billing plan regardless of what is set here.

_Returns_:

Up to date metadata about the updated database.

<hr>

#### `bitdotio.delete_database(db_name)`

Delete a database. After deletion the database's name will be unusable for up to 30
days. If you need to reuse it sooner, please contact bit.io support.

_Args_:
- `db_name (str)`: Name of the database to delete

_Returns_:

None.

<hr>

#### `bitdotio.create_import_job(db_name, table_name, schema_name=None, infer_header=None, file=None, file_url=None)`

Start a data import job from a file or a URL. Supported filetypes CSV, JSON, XLS/XLSX,
and SQLite.

_Args_:
- `db_name (str)`: Name of the database to import data into
- `table_name (str)`: Name of the table to import data into
- `schema_name (Optional[str])`: Name schema in which the target table resides. Not
  required if the table is in the `public` schema.
- `infer_header (Optional[str])`: If relevant to the given filetype, indicates how the
  first row of the data should be interpreted. Should be one of `auto`, `first_row`, or
  `no_header`. If `auto`, we will attempt to determine automatically if there is a
  header or not. If `first_row`, the first row of the data will be used as the header.
  If `no_header`, the first row of the data will be interpreted as data.
- `file (Optional[file-like])`: A file-like object to upload. If this is passed,
  `file_url` must not be passsed.
- `file_url (Optional[str])`: A URL to import a file from. The URL should point to a
  supported filetype on the web. If this is passed, `file` must not be passed.

_Returns_:

A dict describing the status of the import job. The dict contains the fields `id`, and
`status_url`. The value of `id` can be passed to `get_import_job` to get the updated
status of the import job. `status_url` can also be requested directly to get the same.
Also included is the `state` field, which indicates the current status of the job.
Possible values of `state` are `RECEIVED`, `PROCESSING`, `DONE`, and `FAILED`.

<hr>

#### `bitdotio.get_import_job(import_id)`

Retrieves the status and other metadata about a given data import job. See the docs for
`create_import_job` for more details on import job statuses and metadata fields.

_Args_:
- `import_id (str)`: The ID of the import job to retrieve info for.

_Returns_:

A dict describing the status and metadata of an import job.

<hr>

#### `bitdotio.create_export_job(db_name, query_string=None, table_name=None, schema_name=None, file_name=None, export_format=None)`

Start a data export job from a query or a full table. Supported export filetypes are
CSV, JSON, XLS, and Parquet.

_Args_:
- `db_name (str)`: Name of the database to export data from
- `query_string (Optional[str])`: A query to export results for. Providing this option
   will run the query on your database. If this is passed, `table_name` and `schema_name`
   must not be passed.
- `table_name (Optional[str])`: Name of the table to export data from. If this is
  passed, `query_string` must not be passed.
- `schema_name (Optional[str])`: Name schema in which the exported table resides. Not
  required if the table is in the `public` schema.
- `file_name (Optional[str])`: Name of the exported file.
- `export_format (str)`: File format to export data to. Accepted values are `csv`,
  `json`, `xls`, and `parquet`. Defaults to `csv`.

_Returns_:

A dict describing the status of the export job. The dict contains the fields `id`, and
`status_url`. The value of `id` can be passed to `get_export_job` to get the updated
status of the export job. `status_url` can also be requested directly to get the same.
Also included is the `state` field, which indicates the current status of the job.
Possible values of `state` are `RECEIVED`, `PROCESSING`, `DONE`, and `FAILED`. When
the status of the job reaches `DONE`, the field `download_url` will have a non-null
value, and the exported file can be downloaded from it.

<hr>

#### `bitdotio.get_export_job(export_id)`

Retrieves the status and other metadata about a given data export job. See the docs for
`create_export_job` for more details on export job statuses and metadata fields.

_Args_:
- `export_id (str)`: The ID of the export job to retrieve info for.

_Returns_:

A dict describing the status and metadata of an export job.

<hr>

#### `bitdotio.list_service_accounts()`

List metadata pertaining to service accounts the requester has created.

_Returns_:

List of dictionaries describing service account metadata.

<hr>

#### `bitdotio.get_service_account(service_account_id)`

Get metadata about a single service account

_Args_:

- `service_account_id (str)`: ID of the service account

_Returns_:

Dictionary describing service account metadata.

<hr>

#### `bitdotio.create_service_account_key(service_account_id)`

Create a new API key/database password for a given service account

_Args_:

- `service_account_id (str)`: ID of the service account

_Returns_:

Dictionary containing newly created credentials

<hr>

#### `bitdotio.revoke_service_account_keys(service_account_id)`

Revoke all API keys/database passwords for the given service account

_Args_:

- `service_account_id (str)`: ID of the service account

_Returns_: None

<hr>

#### `bitdotio.create_key()`

Create a new API key/database password with the same permissions as the requester

_Returns_:

Dictionary containing newly created credentials

<hr>

#### `bitdotio.revoke_keys(api_key=None)`

Revoke API keys/database passwords. If `api_key` is given, only that API key will
be revoked. Otherwise, all API keys for the requester will be revoked.

_Kwargs_:
- `api_key (Optional[str])`: API key to revoke

_Returns_: None

<hr>
