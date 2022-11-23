import unittest

from unittest.mock import Mock, patch

from bitdotio.api_client import ApiClient
from bitdotio._bitdotio import API_VERSION


class TestApiClient(unittest.TestCase):
    token = "v2_testtoken"

    def setUp(self) -> None:
        self.api_client = ApiClient(self.token, API_VERSION)

    def test_init(self) -> None:
        self.assertEqual(self.api_client._access_token, self.token)
        self.assertEqual(self.api_client._api_version, API_VERSION)
        self.assertIsNotNone(self.api_client._session)
        headers = self.api_client._session.headers
        self.assertEqual(headers["Accept"], "application/json")
        self.assertEqual(headers["Authorization"], f"Bearer {self.token}")

    def test_url(self) -> None:
        expected = f"https://api.bit.io/{API_VERSION}/foo/bar"
        result = self.api_client._url("/foo/bar")
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.Session.request")
    def test_request(self, mock_request: Mock) -> None:
        url = "/foo"
        expected_url = f"https://api.bit.io/{API_VERSION}/foo"
        test_cases = [
            ("GET", None),
            ("POST", {"foo": "bar"}),
            ("PATCH", {"foo": "bar"}),
            ("DELETE", None),
        ]
        for method, body in test_cases:
            self.api_client.request(method, url, json=body)
            mock_request.assert_called_with(method, expected_url, json=body)

    @patch("bitdotio.api_client.Session.request")
    def test_get(self, mock_request: Mock) -> None:
        url = "/foo"
        expected_method = "GET"
        expected_url = f"https://api.bit.io/{API_VERSION}/foo"
        self.api_client.get(url)
        mock_request.assert_called_once_with(expected_method, expected_url)

    @patch("bitdotio.api_client.Session.request")
    def test_post(self, mock_request: Mock) -> None:
        url = "/foo"
        expected_method = "POST"
        expected_url = f"https://api.bit.io/{API_VERSION}/foo"
        body = {"foo": "bar"}
        self.api_client.post(url, json=body)
        mock_request.assert_called_once_with(expected_method, expected_url, json=body)

    @patch("bitdotio.api_client.Session.request")
    def test_patch(self, mock_request: Mock) -> None:
        url = "/foo"
        expected_method = "PATCH"
        expected_url = f"https://api.bit.io/{API_VERSION}/foo"
        body = {"foo": "bar"}
        self.api_client.patch(url, json=body)
        mock_request.assert_called_once_with(expected_method, expected_url, json=body)

    @patch("bitdotio.api_client.Session.request")
    def test_delete(self, mock_request: Mock) -> None:
        url = "/foo"
        expected_method = "DELETE"
        expected_url = f"https://api.bit.io/{API_VERSION}/foo"
        self.api_client.delete(url)
        mock_request.assert_called_once_with(expected_method, expected_url)
