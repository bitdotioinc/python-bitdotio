import unittest
from unittest.mock import Mock, patch

from bitdotio import bitdotio
from bitdotio._bitdotio import ApiError


class TestApiMethods(unittest.TestCase):
    token = "v2_testtoken"

    def setUp(self) -> None:
        self.b = bitdotio(self.token)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_query_ok(self, mock_request: Mock) -> None:
        db_name = "my/db"
        query_str = "SELECT 1"
        data_format = "objects"
        expected = {"foo": "bar"}
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected

        result = self.b.query("my/db", "SELECT 1")

        # Test without data_format
        self.assertEqual(result, expected)
        mock_request.assert_called_once_with(
            "POST",
            "/query",
            json={"database_name": db_name, "query_string": query_str},
        )

        mock_request.reset_mock()

        # Test with data_format
        result = self.b.query("my/db", "SELECT 1", data_format=data_format)
        self.assertEqual(result, expected)
        mock_request.assert_called_once_with(
            "POST",
            f"/query?data_format={data_format}",
            json={"database_name": db_name, "query_string": query_str},
        )

    @patch("bitdotio.api_client.ApiClient.request")
    def test_query_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.query("my/db", "SELECT 1")
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

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
