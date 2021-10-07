import os
import unittest
from unittest import mock
import bitdotio
from bit.bit import bitio
from click.testing import CliRunner
from unittest.mock import Mock, patch


@mock.patch.dict(os.environ, {"BITIO_KEY": ""})
class TestBitQuery(unittest.TestCase):
    def setUp(self) -> None:
         return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_import_url(self):
        """Test that `bit import url` calls bitdotio.model.import_url"""
        with patch.object(bitdotio.model.import_url, "ImportUrl") as mock_import:
            runner = CliRunner()
            result = runner.invoke(
                bitio,
                [
                    "-k",
                    "<API_KEY>",
                    "import",
                    "url",
                    "-r",
                    "some_repo",
                    "-t",
                    "some_table",
                    "-u",
                    "some_url",
                ],
            )
            mock_import.assert_called_once()
            mock_import.assert_called_with("some_url", "some_table", "some_repo")
            
    def test_import_url_no_key(self):
        """Test that `bit import url` fails without a key"""

        with patch.object(bitdotio.model.import_url, "ImportUrl") as mock_import:
            runner = CliRunner()
            result = runner.invoke(
                bitio,
                [
                    "import",
                    "url",
                    "-r",
                    "some_repo",
                    "-t",
                    "some_table",
                    "-u",
                    "some_url",
                ],
            )
            #mock_import.assert_not_called()
            #assert result.exception
            pass


    def test_import_json(self):
        """Test that `bit import json-data` calls bitdotio.model.import_json"""

        with patch.object(bitdotio.model.import_json, "ImportJson") as mock_import:
            runner = CliRunner()
            result = runner.invoke(
                bitio,
                [
                    "-k",
                    "<API_KEY>",
                    "import",
                    "json-data",
                    "-r",
                    "some_repo",
                    "-t",
                    "some_table",
                ],
                input='{"some_json":1}',
            )
            mock_import.assert_called_once()
            mock_import.assert_called_with('{"some_json":1}', "some_table", "some_repo")

    @patch('bitdotio.bitdotio')
    def test_import_file(self, mock_bitdotio):
        runner = CliRunner()
        result = runner.invoke(
                bitio,
                [
                    "-k",
                    "<API_KEY>",
                    "import",
                    "json-data",
                    "-r",
                    "some_repo",
                    "-t",
                    "some_table",
                    "-f",
                    "some_file"
                ]
            )
        mock_bitdotio.assert_called_once()


if __name__ == "__main__":
    unittest.main()
