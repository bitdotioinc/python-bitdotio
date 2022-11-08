import os
import unittest
import tempfile
from unittest.mock import Mock, patch

from bit.bit import bitio
from click.testing import CliRunner

"""
click.testing.CliRunner is not thread safe! This will likely cause
future tests affecting interpreter state to fail.

`bitio.params[0].required = True` in teardown addresses the case where
a test of '--help' functionality without a key changes the bitio 'key'
parameter requirement to "False," causing later tests of the key
requirement to fail.
"""


@patch.dict(os.environ, {"BITIO_KEY": ""})
class TestCLI(unittest.TestCase):
    # Test token that passes regex validation
    token = "v2_testtoken"

    def setUp(self) -> None:
        self.runner = CliRunner()

    def tearDown(self) -> None:
        bitio.params[0].required = True

    def cmd(self, *args):
        return ["-k", self.token, *args]

    def test_help(self):
        result = self.runner.invoke(bitio, ["--help", "bitio"])
        self.assertEqual(result.exit_code, 0)

    def test_no_args(self):
        """Test that bit with no arguments returns same as with --help"""
        res1 = self.runner.invoke(bitio)
        res2 = self.runner.invoke(bitio, ["--help", "bitio"])
        self.assertEqual(res1.output, res2.output)

    def test_help_no_key(self):
        """Test that help for query, import, repo commands are accessible without key"""
        query_result = self.runner.invoke(bitio, ["query", "--help", "bitio"])
        db_result = self.runner.invoke(bitio, ["db", "--help", "bitio"])

        self.assertEqual(query_result.exit_code, 0)
        self.assertEqual(db_result.exit_code, 0)

    @patch("bitdotio._bitdotio._BitV2.get_database", return_value={})
    def test_bitio_key_env_var(self, mock_get_database: Mock):
        # Check that we can omit -k/--key and use BITIO_KEY env var instead. Use db
        # info command for this purpose since it's the simplest.
        os.environ["BITIO_KEY"] = self.token
        cmd = ["db", "info", "-d", "my/db"]
        result = self.runner.invoke(bitio, cmd)
        self.assertEqual(result.exit_code, 0)
        mock_get_database.assert_called_once()
        del os.environ["BITIO_KEY"]

    @patch("bitdotio._bitdotio._BitV2.query", return_value={})
    def test_query_ok_query_str(self, mock_query: Mock):
        cmd = self.cmd("query", "-d", "my/db", "-q", "select 1")
        result = self.runner.invoke(bitio, cmd)
        self.assertEqual(result.exit_code, 0)
        mock_query.assert_called_once_with("my/db", "select 1")

    @patch("bitdotio._bitdotio._BitV2.query", return_value={})
    def test_query_ok_query_file(self, mock_query: Mock):
        query = "select 1"
        with tempfile.TemporaryDirectory() as temp_path:
            file_path = os.path.join(temp_path, "query.sql")
            with open(file_path, "w+") as f:
                f.write(query)

            cmd = self.cmd("query", "-d", "my/db", "-qf", file_path, "-o")
            result = self.runner.invoke(bitio, cmd)
            self.assertEqual(result.exit_code, 0)
            mock_query.assert_called_once_with(
                "my/db", "select 1", data_format="objects"
            )

    def test_query_error(self):
        test_cases = [("-d", "my/db"), ("-q", "select 1", "-o"), ("-qf", "file.sql")]
        for test_case in test_cases:
            cmd = self.cmd("query", *test_case)
            result = self.runner.invoke(bitio, cmd)
            self.assertNotEqual(result.exit_code, 0)

    @patch("bitdotio._bitdotio._BitV2.list_databases", return_value=[])
    def test_db_list_ok(self, mock_list_databases: Mock):
        cmd = self.cmd("db", "list")
        result = self.runner.invoke(bitio, cmd)
        self.assertEqual(result.exit_code, 0)
        mock_list_databases.assert_called_once()

    @patch("bitdotio._bitdotio._BitV2.create_database", return_value=[])
    def test_db_create_ok(self, mock_create_database: Mock):
        cmd = self.cmd("db", "create", "-n", "my/db", "-p", "false")
        result = self.runner.invoke(bitio, cmd)
        self.assertEqual(result.exit_code, 0)
        mock_create_database.assert_called_once_with("my/db", is_private=False)

    def test_db_create_error(self):
        cmd = self.cmd("db", "create", "-p", "false")
        result = self.runner.invoke(bitio, cmd)
        self.assertNotEqual(result.exit_code, 0)

    @patch("bitdotio._bitdotio._BitV2.get_database", return_value=[])
    def test_db_info_ok(self, mock_get_database: Mock):
        cmd = self.cmd("db", "info", "-d", "my/db")
        result = self.runner.invoke(bitio, cmd)
        self.assertEqual(result.exit_code, 0)
        mock_get_database.assert_called_once_with("my/db")

    def test_db_info_error(self):
        cmd = self.cmd("db", "info")
        result = self.runner.invoke(bitio, cmd)
        self.assertNotEqual(result.exit_code, 0)

    @patch("bitdotio._bitdotio._BitV2.update_database", return_value=[])
    def test_db_update_ok(self, mock_update_database: Mock):
        test_cases = [
            [],
            ("-p", "false"),
            ("-n", "your/db"),
            ("-n", "your/db", "-p", "false"),
        ]
        for test_case in test_cases:
            cmd = self.cmd("db", "update", "-d", "my/db", *test_case)
            result = self.runner.invoke(bitio, cmd)
            self.assertEqual(result.exit_code, 0)
            mock_update_database.assert_called_once()
            mock_update_database.reset_mock()

    def test_db_update_error(self):
        cmd = self.cmd("db", "update", "-p", "false")
        result = self.runner.invoke(bitio, cmd)
        self.assertNotEqual(result.exit_code, 0)

    @patch("bitdotio._bitdotio._BitV2.delete_database", return_value=[])
    def test_db_delete_ok(self, mock_delete_database: Mock):
        cmd = self.cmd("db", "delete", "-d", "my/db")
        result = self.runner.invoke(bitio, cmd)
        self.assertEqual(result.exit_code, 0)
        mock_delete_database.assert_called_once_with("my/db")

    def test_db_delete_error(self):
        cmd = self.cmd("db", "delete")
        result = self.runner.invoke(bitio, cmd)
        self.assertNotEqual(result.exit_code, 0)
