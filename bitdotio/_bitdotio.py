#!/usr/bin/env python3
import functools
import sys
import typing as t
from contextlib import contextmanager

from requests import Response

from bitdotio.api_client import ApiClient
from bitdotio.utils import validate_database_name, validate_min_max_conn, validate_token

API_VERSION = "v2beta"


def bitdotio(
    access_token: str,
    api_version: str = API_VERSION,
    min_conn: int = 0,
    max_conn: int = 100,
):
    return _BitV2(access_token, api_version, min_conn, max_conn)


class ApiError(Exception):
    def __init__(self, status_code: int, data: t.Any) -> None:
        self.status_code = status_code
        self.data = data

    def __str__(self) -> str:
        return f"ApiError status_code={self.status_code} data={self.data}"


def api_method(
    returning: t.Optional[str] = None,
) -> t.Callable[[t.Callable[..., Response]], t.Callable[..., t.Any]]:
    def decorator(method: t.Callable[..., Response]) -> t.Callable[..., t.Any]:
        @functools.wraps(method)
        def wrapper(*args, **kwargs):
            response = method(*args, **kwargs)
            body = response.json()
            if response.ok:
                if returning:
                    return body[returning]
                return body

            raise ApiError(response.status_code, body)

        return wrapper

    return decorator


class _BitV2:

    _port = 5432
    _host = "db.bit.io"

    def __init__(
        self,
        access_token: str,
        api_version: str,
        min_conn: int,
        max_conn: int,
    ) -> None:
        validate_token(access_token)
        validate_min_max_conn(min_conn, max_conn)

        self._access_token = access_token
        self._api_client = ApiClient(access_token, api_version)
        self._min_conn = min_conn
        self._max_conn = max_conn

        self._pools = {}

    def __repr__(self):
        return "<bitdotio SDK object: v2>"

    def _get_conn_string(self, db_name):
        db = db_name
        user = "api_user"
        password = self._access_token
        host = self._host
        port = self._port
        return f"dbname={db} user={user} password={password} host={host} port={port} sslmode=require"

    @staticmethod
    def _create_pool(pool_cls, *args, **kwargs):
        """This is super weird code factorization but it's necessary in order to mock
        out the connection pool in testing. We can't mock ThreadedConnectionPool
        directly since it's not imported at the module level.
        """
        return pool_cls(*args, **kwargs)

    def _get_pool(self, db_name: str):
        pool = self._pools.get(db_name)
        if pool is not None:
            return pool

        try:
            # Threadsafe by default
            from psycopg2.pool import ThreadedConnectionPool
        except ImportError as exc:
            _print_psycopg2_message()
            raise exc

        conn_string = self._get_conn_string(db_name)
        pool = self._create_pool(
            ThreadedConnectionPool,
            self._min_conn,
            self._max_conn,
            conn_string,
        )
        self._pools[db_name] = pool
        return pool

    def get_connection(self, db_name):
        try:
            import psycopg2
        except ImportError as e:
            _print_psycopg2_message()
            raise e

        conn_str = self._get_conn_string(db_name)
        conn = psycopg2.connect(conn_str)

        return conn

    @contextmanager
    def pooled_connection(self, db_name: str):
        pool, conn = None, None
        try:
            pool = self._get_pool(db_name)
            conn = pool.getconn()
            yield conn
        finally:
            if pool is not None and conn is not None:
                pool.putconn(conn)

    @contextmanager
    def pooled_cursor(self, db_name: str):
        with self.pooled_connection(db_name) as conn:
            with conn.cursor() as cursor:
                yield cursor

    @api_method()
    def query(self, db_name: str, query_str: str, data_format: t.Optional[str] = None):
        url = f"/query"
        if data_format is not None:
            url += f"?data_format={data_format}"

        request_body = {"database_name": db_name, "query_string": query_str}

        return self._api_client.post(url, json=request_body)

    @api_method(returning="databases")
    def list_databases(self):
        return self._api_client.get("/db/")

    @api_method()
    def create_database(
        self,
        name: str,
        is_private: bool = True,
        storage_limit_bytes: t.Optional[int] = None,
    ):
        request_body = {"name": name, "is_private": is_private}
        if storage_limit_bytes:
            request_body["storage_limit_bytes"] = storage_limit_bytes

        return self._api_client.post("/db/", json=request_body)

    @api_method()
    def get_database(self, db_name: str):
        validate_database_name(db_name)
        return self._api_client.get(f"/db/{db_name}")

    @api_method()
    def update_database(
        self,
        db_name: str,
        name: t.Optional[str] = None,
        is_private: t.Optional[bool] = None,
        storage_limit_bytes: t.Optional[int] = None,
    ):
        validate_database_name(db_name)
        request_body = {
            k: v
            for k, v in {
                "name": name,
                "is_private": is_private,
                "storage_limit_bytes": storage_limit_bytes,
            }.items()
            if v is not None
        }

        return self._api_client.patch(f"/db/{db_name}", json=request_body)

    @api_method()
    def delete_database(self, db_name: str):
        validate_database_name(db_name)
        return self._api_client.delete(f"/db/{db_name}")


def _print_psycopg2_message():
    print(
        """
It looks like we couldn't import the psycopg2 library!

In order to support different environments, we have a few ways to install the bitdotio package
with or without the psycopg2 dependency.

1. If you already have psycopg2 install, you can install the default bitdotio package:

  pip install bitdotio

2. If you already have Postgres installed, you can install with the psycopg2 dependency:

  pip install bitdotio[psycopg2]

3. If you do not have or cannot install Postgres, you can install with the psycopg2-binary dependency:

  pip install bitdotio[psycopg2-binary]

""",
        file=sys.stderr,
    )
