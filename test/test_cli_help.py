import os
import unittest
from unittest import mock

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
class TestBitHelp(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        bitio.params[0].required = True
        return super().tearDown()

    def test_help(self):
        runner = CliRunner()
        result = runner.invoke(bitio, ["--help", "bitio"])
        assert result.exit_code == 0

    def test_no_args(self):
        """Test that bit with no arguments returns same as with --help"""
        runner = CliRunner()
        res1 = runner.invoke(bitio)
        res2 = runner.invoke(bitio, ["--help", "bitio"])
        assert res1.output == res2.output

    def test_help_no_key(self):
        """Test that help for query, import, repo commands are accessible without key"""
        runner = CliRunner()
        query_result = runner.invoke(bitio, ["query", "--help", "bitio"])
        import_result = runner.invoke(bitio, ["import", "--help", "bitio"])
        repo_result = runner.invoke(bitio, ["repo", "--help", "bitio"])

        assert query_result.exit_code == 0
        assert import_result.exit_code == 0
        assert repo_result.exit_code == 0


if __name__ == "__main__":
    unittest.main()
