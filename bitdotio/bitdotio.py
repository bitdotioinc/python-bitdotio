#!/usr/bin/env python3
import functools
import sys
import typing as t

from requests import Response

from bitdotio.api_client import ApiClient
from bitdotio.utils import validate_database_name, validate_token

API_VERSION = "v2beta"


def bitdotio(
    access_token: str,
    api_version: str = API_VERSION,
):
    return _BitV2(access_token, api_version)


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

    def __init__(self, access_token: str, api_version: str) -> None:
        validate_token(access_token)

        self._access_token = access_token
        self._api_client = ApiClient(access_token, api_version)

    def __repr__(self):
        return "<bitdotio SDK object: v2>"

    def _token_to_creds(self, database_name):
        db = database_name
        user = "api_user"
        password = self._access_token
        host = self._host
        port = self._port
        return f"dbname={db} user={user} password={password} host={host} port={port} sslmode=require"

    def get_connection(self, database_name):
        try:
            import psycopg2
        except ImportError as e:
            _print_psycopg2_message()
            raise e

        conn_str = self._token_to_creds(database_name)
        conn = psycopg2.connect(conn_str)

        return conn

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
