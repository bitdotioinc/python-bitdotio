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

    def test_query(self):
        with patch.object(bitdotio.model.query, "Query") as mock_query:
            runner = CliRunner()
            result = runner.invoke(
                bitio, ["-k", "<API_KEY>", "query", "--query", "Some Query Text"]
            )
            mock_query.assert_called_once()
            mock_query.assert_called_with(query_string="Some Query Text")

    def test_query_no_key(self):
        with patch.object(bitdotio.model.query, "Query") as mock_query:
            runner = CliRunner()
            result = runner.invoke(bitio, ["query", "--query", "Some Query Text"])
            #mock_query.assert_not_called()
            #assert result.exception
            pass


if __name__ == "__main__":
    unittest.main()
