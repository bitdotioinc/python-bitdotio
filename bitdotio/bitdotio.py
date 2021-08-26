#!/usr/bin/env python3
from __future__ import print_function
import time
import bitdotio
from bitdotio import Configuration, ApiClient, ApiBitdotio
from bitdotio.rest import ApiException
import psycopg2
from pprint import pprint


def bitdotio(access_token):
    return _Bit(access_token)

class _Bit(ApiBitdotio):
    _port = 5432
    _host = "db.bit.io"
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

    def _token_to_creds(self):
        # Both _user_ and _db_ here are to satisfy psycopg2, but bit.io itself
        # doesn't care about these - everything we need is in the access token.
        db = "qap"
        user = "api_user"
        password = self.access_token
        host = self._host
        port = self._port
        return f"dbname={db} user={user} password={password} host={host} port={port}"

    def get_connection(self):
        conn_str = self._token_to_creds()
        conn = psycopg2.connect(self._token_to_creds())
        conn.autocommit = True

        return conn
