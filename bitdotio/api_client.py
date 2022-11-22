import typing as t
from urllib.parse import urljoin

from requests import Response, Session

from bitdotio._version import __version__


class ApiClient:

    __slots__ = ("_access_token", "_api_version", "_session")

    def __init__(self, access_token: str, api_version: str) -> None:
        self._access_token = access_token
        self._api_version = api_version

        self._session = Session()
        self._session.headers.update(
            {
                "Accept": "application/json",
                "Authorization": f"Bearer {self._access_token}",
                "User-Agent": f"python-bitdotio-sdk/{__version__}"
            }
        )

    def _url(self, path: str) -> str:
        return urljoin(f"https://api.bit.io", f"{self._api_version}{path}")

    def request(self, method: str, url: str, **kwargs: t.Any) -> Response:
        return self._session.request(method, self._url(url), **kwargs)

    def get(self, url: str, **kwargs: t.Any) -> Response:
        return self.request("GET", url, **kwargs)

    def post(self, url: str, json: t.Any = None, **kwargs: t.Any) -> Response:
        return self.request("POST", url, json=json, **kwargs)

    def patch(self, url: str, json: t.Any = None, **kwargs: t.Any) -> Response:
        return self.request("PATCH", url, json=json, **kwargs)

    def delete(self, url: str, **kwargs: t.Any) -> Response:
        return self.request("DELETE", url, **kwargs)

    def set_header(self, header: str, value: str) -> None:
        self._session.headers.update({header: value})
