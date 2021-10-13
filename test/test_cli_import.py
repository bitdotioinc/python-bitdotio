import os
import unittest
from unittest import mock
from unittest.mock import Mock, patch

import bitdotio
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


@mock.patch.dict(os.environ, {"BITIO_KEY": ""})
class TestBitQuery(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        bitio.params[0].required = True
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
        with patch.object(bitdotio.model.import_url, "ImportUrl") as mock_import_no_key:
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
            mock_import_no_key.assert_not_called()
            assert result.exception

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

    @patch("bitdotio.bitdotio")
    def test_import_file(self, mock_bitdotio):
        runner = CliRunner()
        runner.invoke(
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
                "some_file",
            ],
        )
        mock_bitdotio.assert_called_once()
        mock_bitdotio.assert_called_with("<API_KEY>")


if __name__ == "__main__":
    unittest.main()
