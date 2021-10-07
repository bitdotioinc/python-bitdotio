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
    
    def test_import_file(self):
        with patch.object(bitdotio.model.import_url, 'ImportUrl') as mock_import:
            runner = CliRunner()
            result = runner.invoke(bitio, ['-k', '<API_KEY>', 'import', 'url',
            '-r', 'some_repo', '-t', 'some_table', '-u', 'some_url'])
            mock_import.assert_called_once()
            mock_import.assert_called_with('some_url', 'some_table', 'some_repo')

    def test_import_file_no_key(self):
        with patch.object(bitdotio.model.import_url, 'ImportUrl') as mock_import:
            runner = CliRunner()
            result = runner.invoke(bitio, ['import', 'url',
            '-r', 'some_repo', '-t', 'some_table', '-u', 'some_url'])
            mock_import.assert_not_called()
            assert result.exception        

if __name__ == "__main__":
    unittest.main()
