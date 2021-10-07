from click.testing import CliRunner
import bitdotio
import bit
from bit.bit import bitio
import unittest

class TestBitHelp(unittest.TestCase): 
    def test_help(self):
        runner = CliRunner()
        result = runner.invoke(bitio, ['--help', 'bitio'])
        assert result.exit_code == 0

    def test_no_args(self):
        runner=CliRunner()
        res1 = runner.invoke(bitio)
        res2 = runner.invoke(bitio, ['--help', 'bitio'])
        assert res1.output == res2.output



if __name__ == '__main__':
    unittest.main()

