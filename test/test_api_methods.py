import io
import unittest
import uuid
from unittest.mock import Mock, patch, ANY

from requests_toolbelt import MultipartEncoder

from bitdotio import bitdotio
from bitdotio._bitdotio import ApiError


class ApiTestCase(unittest.TestCase):
    token = "v2_testtoken"

    def setUp(self) -> None:
        self.b = bitdotio(self.token)


class TestApiMethods(ApiTestCase):
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
    def test_delete_database_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.delete_database("my/db")
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_list_service_accounts_ok(self, mock_request: Mock) -> None:
        expected = ["foo", "bar"]
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {"service_accounts": expected}
        result = self.b.list_service_accounts()
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_list_service_accounts_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.list_service_accounts()
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_get_service_acount_ok(self, mock_request: Mock) -> None:
        expected = {"foo": "bar"}
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected
        result = self.b.get_service_account(str(uuid.uuid4()))
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_get_service_account_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.get_service_account(str(uuid.uuid4()))
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_service_account_key_ok(self, mock_request: Mock) -> None:
        expected = {"foo": "bar"}
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected
        result = self.b.create_service_account_key(str(uuid.uuid4()))
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_service_account_key_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.create_service_account_key(str(uuid.uuid4()))
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_revoke_service_account_keys_ok(self, mock_request: Mock) -> None:
        expected = None
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected
        result = self.b.revoke_service_account_keys(str(uuid.uuid4()))
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_revoke_service_account_keys_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.revoke_service_account_keys(str(uuid.uuid4()))
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_key_ok(self, mock_request: Mock) -> None:
        expected = {"foo": "bar"}
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected
        result = self.b.create_key()
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_key_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.create_key()
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_revoke_keys_ok_all(self, mock_request: Mock) -> None:
        expected = None
        expected_url = "/api-key/"
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected
        result = self.b.revoke_keys()
        self.assertEqual(result, expected)
        mock_request.assert_called_once_with("DELETE", expected_url)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_revoke_keys_ok_single(self, mock_request: Mock) -> None:
        expected = None
        expected_url = f"/api-key/?api_key={self.token}"
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = expected
        result = self.b.revoke_keys(self.token)
        self.assertEqual(result, expected)
        mock_request.assert_called_once_with("DELETE", expected_url)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_revoked_keys_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.revoke_keys()
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)


class TestImports(ApiTestCase):
    @patch("requests_toolbelt.multipart.encoder.uuid4")
    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_import_job_file_ok(
        self, mock_request: Mock, mock_uuid4: Mock
    ) -> None:
        mock_uuid4.return_value = uuid.uuid4()

        file = io.BytesIO(b"foo")
        mock_request.return_value.ok = True
        mock_request.return_value.json.return_value = {"foo": "bar"}
        self.b.create_import_job("my/db", "table", infer_header="first_row", file=file)
        data = {"table_name": "table", "infer_header": "first_row"}
        data = MultipartEncoder(
            fields={
                "file": (data["table_name"], file),
                **data,
            }
        )
        mock_request.assert_called_once_with(
            "POST",
            "/db/my/db/import/",
            json=None,
            data=ANY,
            headers={"Content-Type": data.content_type},
        )
        self.assertEqual(
            data.fields,
            mock_request.call_args.kwargs["data"].fields,
        )

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_import_job_url_ok(self, mock_request: Mock) -> None:
        url = "https://example.org/file.csv"
        mock_request.return_value.ok = True
        mock_request.return_value.json.return_value = {"foo": "bar"}
        self.b.create_import_job("my/db", "table", schema_name="schema", file_url=url)
        mock_request.assert_called_once_with(
            "POST",
            "/db/my/db/import/",
            json=None,
            data={"table_name": "table", "schema_name": "schema", "file_url": url},
            headers={},
        )

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_import_job_invalid_db_name(self, _: Mock) -> None:
        with self.assertRaisesRegex(ValueError, "Invalid database name"):
            self.b.create_import_job(
                "mydb",
                "mytable",
                file_url="https://example.org/myfile.csv",
            )

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_import_job_missing_file_and_url(self, _: Mock) -> None:
        with self.assertRaisesRegex(ValueError, "Must provide file XOR file_url"):
            self.b.create_import_job(
                "my/db",
                "mytable",
            )

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_import_job_both_file_and_url(self, _: Mock) -> None:
        with self.assertRaisesRegex(ValueError, "Must provide file XOR file_url"):
            self.b.create_import_job(
                "my/db",
                "mytable",
                file=io.BytesIO(b"foo"),
                file_url="https://example.org/myfile.csv",
            )

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_import_job_error(self, mock_request: Mock) -> None:
        url = "https://example.org/file.csv"
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.create_import_job("my/db", "table", file_url=url)
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_get_import_job_ok(self, mock_request: Mock) -> None:
        expected = {"foo", "bar"}
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 201
        mock_request.return_value.json.return_value = expected
        result = self.b.get_import_job(str(uuid.uuid4()))
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_get_import_job_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.get_import_job(str(uuid.uuid4()))
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)


class TestExports(ApiTestCase):
    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_export_job_query_ok(self, mock_request: Mock) -> None:
        mock_request.return_value.ok = True
        mock_request.return_value.json.return_value = {"foo": "bar"}
        self.b.create_export_job("my/db", query_string="select 1", file_name="foo.csv")
        mock_request.assert_called_once_with(
            "POST",
            "/db/my/db/export/",
            json={
                "query_string": "select 1",
                "file_name": "foo.csv",
                "export_format": "csv",
            },
        )

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_export_job_table_ok(self, mock_request: Mock) -> None:
        mock_request.return_value.ok = True
        mock_request.return_value.json.return_value = {"foo": "bar"}
        self.b.create_export_job(
            "my/db",
            table_name="table",
            schema_name="schema",
            export_format="parquet",
        )
        mock_request.assert_called_once_with(
            "POST",
            "/db/my/db/export/",
            json={
                "table_name": "table",
                "schema_name": "schema",
                "export_format": "parquet",
            },
        )

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_export_job_table_no_schema_ok(self, mock_request: Mock) -> None:
        mock_request.return_value.ok = True
        mock_request.return_value.json.return_value = {"foo": "bar"}
        self.b.create_export_job(
            "my/db",
            table_name="table",
            export_format="xls",
        )
        mock_request.assert_called_once_with(
            "POST",
            "/db/my/db/export/",
            json={
                "table_name": "table",
                "schema_name": "public",
                "export_format": "xls",
            },
        )

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_export_job_invalid_db_name(self, _: Mock) -> None:
        with self.assertRaisesRegex(ValueError, "Invalid database name"):
            self.b.create_export_job("mydb", query_string="select 1")

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_export_job_missing_query_and_table(self, _: Mock) -> None:
        with self.assertRaisesRegex(
            ValueError, "Must provide query_string XOR table_name"
        ):
            self.b.create_export_job("my/db")

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_export_job_both_query_and_table(self, _: Mock) -> None:
        with self.assertRaisesRegex(
            ValueError, "Must provide query_string XOR table_name"
        ):
            self.b.create_export_job(
                "my/db",
                query_string="select 1",
                table_name="table",
                schema_name="schema",
            )

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_export_job_missing_table(self, _: Mock) -> None:
        with self.assertRaisesRegex(
            ValueError, "Must provide query_string XOR table_name"
        ):
            self.b.create_export_job("my/db", schema_name="schema")

    @patch("bitdotio.api_client.ApiClient.request")
    def test_create_export_job_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.create_export_job("my/db", query_string="q", export_format="xls")
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_get_export_job_ok(self, mock_request: Mock) -> None:
        expected = {"foo", "bar"}
        mock_request.return_value.ok = True
        mock_request.return_value.status_code = 201
        mock_request.return_value.json.return_value = expected
        result = self.b.get_export_job(str(uuid.uuid4()))
        self.assertEqual(result, expected)

    @patch("bitdotio.api_client.ApiClient.request")
    def test_get_export_job_error(self, mock_request: Mock) -> None:
        status_code = 400
        error_data = {"error": "whoops"}
        mock_request.return_value.ok = False
        mock_request.return_value.status_code = status_code
        mock_request.return_value.json.return_value = error_data
        with self.assertRaises(ApiError) as cm:
            self.b.get_export_job(str(uuid.uuid4()))
            self.assertEqual(cm.exception.status_code, status_code)
            self.assertEqual(cm.exception.data, error_data)
