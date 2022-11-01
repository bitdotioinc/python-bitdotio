#!/usr/bin/env python3
from __future__ import print_function
from inspect import Attribute
import time
import bitdotio
from bitdotio import Configuration, ApiClient, ApiBitdotio
from bitdotio.rest import ApiException
from pprint import pprint
import sys
from . import model


def bitdotio(access_token):
    # determine bit.io version from the token format
    token_parts = access_token.split('_')
    if len(token_parts) == 2:
        return _Bit(access_token)
    elif (len(token_parts) == 3) and (token_parts[0] == 'v2'):
        return _BitV2(access_token)
    else:
        raise ValueError("Invalid access token format.")


class _HostConfigMixin():
    _port = 5432
    _host = "db.bit.io"


class _Bit(_HostConfigMixin, ApiBitdotio):
    def __init__(self, access_token):
        assert access_token
        configuration = Configuration(
            host = "https://api.bit.io/api/v1beta",
        )
        configuration.access_token = access_token
        self.access_token = access_token
        self.api_client = ApiClient(configuration)
        self.api_client.user_agent = "bit.io-SDK/1.0.0/python"
        super().__init__(self.api_client)

    def __repr__(self):
        return "<bitdotio SDK object: v1>"

    def _token_to_creds(self):
        # Both _user_ and _db_ here are to satisfy psycopg2, but bit.io itself
        # doesn't care about these - everything we need is in the access token.
        db = "qap"
        user = "api_user"
        password = self.access_token
        host = self._host
        port = self._port
        return f"dbname={db} user={user} password={password} host={host} port={port}"

    def query(self, query_string, fields={}, data=[]):
        query_obj = model.query.Query(query_string=query_string, fields=fields, data=data)
        return self.create_query(query=query_obj)

    def get_connection(self):
        try:
            import psycopg2
        except ImportError as e:
            _print_psycopg2_message()
            raise e

        conn_str = self._token_to_creds()
        conn = psycopg2.connect(conn_str)
        conn.autocommit = True

        return conn


class _BitV2(_HostConfigMixin):
    _BACKWARDS_INCOMPATIBLE_ATTRIBUTES = [
        'api_client',
        'create_import_file',
        'create_import_json',
        'create_import_url',
        'create_query',
        'create_repo',
        'destroy_repo',
        'list_repos',
        'partial_update_repo',
        'query',
        'retrieve_ingestor_job',
        'retrieve_repo',
        'update_repo',
        ]
    
    def __init__(self, access_token):
        assert access_token
        self.access_token = access_token

    def __repr__(self):
        return "<bitdotio SDK object: v2>"

    # inform user when an attempt is made to access v1-only attribute 
    def __getattr__(self, name):
        if name in self._BACKWARDS_INCOMPATIBLE_ATTRIBUTES:
            raise AttributeError(f"You have configured the SDK with a v2 token, and '{name}' is currently limited to v1.")
        else:
            raise AttributeError(f"'_BitV2' object has no attribute '{name}'")

    def _token_to_creds(self, database_name):
        db = database_name
        user = "api_user"
        password = self.access_token
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

def _print_psycopg2_message():
    print("""
It looks like we couldn't import the psycopg2 library!

In order to support different environments, we have a few ways to install the bitdotio package
with or without the psycopg2 dependency.

1. If you already have psycopg2 install, you can install the default bitdotio package:

  pip install bitdotio

2. If you already have Postgres installed, you can install with the psycopg2 dependency:

  pip install bitdotio[psycopg2]

3. If you do not have or cannot install Postgres, you can install with the psycopg2-binary dependency:

  pip install bitdotio[psycopg2-binary]

""", file=sys.stderr)
