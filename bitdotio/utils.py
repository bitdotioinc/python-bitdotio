import re


_RE_TOKEN = re.compile(r"^v2_\w+$")
_RE_DB_NAME = re.compile(r"^\w.{0,37}?/.{1,23}$")


def validate_token(token: str):
    if _RE_TOKEN.fullmatch(token) is None:
        raise ValueError("Invalid access token")


def validate_database_name(db_name: str):
    if _RE_DB_NAME.fullmatch(db_name) is None:
        raise ValueError("Invalid database name")


def validate_min_max_conn(min_conn: int, max_conn: int):
    if min_conn < 0 or max_conn < 0:
        raise ValueError("min_conn and max_conn must both be greater than or equal to zero")
    if min_conn >= max_conn:
        raise ValueError("min_conn must be strictly less than max_conn")

def prune_body(body: dict) -> dict:
    return {k: v for k, v in body.items() if v is not None}
