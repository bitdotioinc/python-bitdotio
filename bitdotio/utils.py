import re


_RE_TOKEN = re.compile(r"^v2_\w+$")
_RE_DB_NAME = re.compile(r"^\w.{0,37}?/.{1,23}$")


def validate_token(token: str):
    if _RE_TOKEN.fullmatch(token) is None:
        raise ValueError("Invalid access token")


def validate_database_name(db_name: str):
    if _RE_DB_NAME.fullmatch(db_name) is None:
        raise ValueError("Invalid database name")
