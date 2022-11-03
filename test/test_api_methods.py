import unittest
from unittest.mock import Mock, patch

from bitdotio import bitdotio
from bitdotio.bitdotio import ApiError


class TestApiMethods(unittest.TestCase):
    token = "v2_testtoken"

    def setUp(self) -> None:
        self.b = bitdotio(self.token)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_list_databases_ok(self, mock_request: Mock) -> None:
        expected = ["foo", "bar"]
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {"databases": expected}
        result = self.b.list_databases()
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_list_databases_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.list_databases()
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_database_ok(self, mock_request: Mock) -> None:
        expected = {"foo", "bar"}
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 201
        mock_request.return_value.json.return_value = expected
        result = self.b.create_database("my-db")
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_database_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.create_database("my-db")
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_get_database_ok(self, mock_request: Mock) -> None:
        expected = {"foo", "bar"}
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 201
        mock_request.return_value.json.return_value = expected
        result = self.b.get_database("my/db")
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_get_database_invalid_db_name(self, _: Mock) -> None:
        with self.assertRaises(ValueError):
            self.b.get_database("mydb")

    @patch("bitdotio.api_client.ApiClient.request")
    def test_get_database_error(self, mock_request: Mock) -> None:
        status_code = 401
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.get_database("my/db")
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_update_database_ok(self, mock_request: Mock) -> None:
        expected = {"foo", "bar"}
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected
        result = self.b.update_database("my/db", is_private=False)
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_update_database_invalid_db_name(self, _: Mock) -> None:
        with self.assertRaises(ValueError):
            self.b.update_database("mydb", is_private=False)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_update_database_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.update_database("my/db", is_private=False)
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_delete_database_ok(self, mock_request: Mock) -> None:
        expected = {"foo", "bar"}
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected
        result = self.b.delete_database("my/db")
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_delete_database_invalid_db_name(self, _: Mock) -> None:
        with self.assertRaises(ValueError):
            self.b.delete_database("mydb")

    @patch("bitdotio.api_client.ApiClient.request")
    def test_delet_database_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.delete_database("my/db")
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)
