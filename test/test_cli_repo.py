import os
import unittest
from unittest import mock
from unittest.mock import Mock, patch
import bit
from bit.bit import bitio
from click.testing import CliRunner


FAKE_KEY = '1234'


@mock.patch.dict(os.environ, {"BITIO_KEY": ""})
class TestBitHelp(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    @patch('bit.bit.print_json_model_list')
    @patch('bitdotio.bitdotio')
    def test_list_repos(self, mock_bitdotio, mock_print_json):
        runner = CliRunner()
        result = runner.invoke(bitio, ["-k", FAKE_KEY, "repo", "list"])
        mock_bitdotio.assert_called_once()
        mock_print_json.assert_called_once()


    @patch('bit.bit.print_json_model')
    @patch('bitdotio.bitdotio')
    def test_retrieve_repo(self, mock_bitdotio, mock_print_json):
        runner = CliRunner()
        result = runner.invoke(bitio, ["-k", FAKE_KEY, "repo", "retrieve", "-r", "repo_name"])
        mock_bitdotio.assert_called_once()
        mock_print_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()

