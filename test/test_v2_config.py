import os
import unittest

import bitdotio
from bitdotio.bitdotio import _Bit, _BitV2

"""
Tests automatic SDK configuration based on token version and v1-only attribute messages.
"""


class TestTokenVersionConfig(unittest.TestCase):

    def test_v1_token(self):
        """Test that v1 formatted token causes v1 object construction"""
        b = bitdotio.bitdotio("3UPuN_fakeTOKENDDPEBNp7Cux7gy")
        self.assertIsInstance(b, _Bit)

    def test_v2_token(self):
        """Test that v2 formatted token causes v2 object construction"""
        b = bitdotio.bitdotio("v2_5_fakeTOKENWxwNLWZvWCXi6c")
        self.assertIsInstance(b, _BitV2)

    def test_invalid_token(self):
        """Test that invalid token format raises value error"""
        with self.assertRaises(ValueError):
            b = bitdotio.bitdotio("v2_5_fakeTOKENWx_wNLWZvWCXi6c")
            self.assertIsInstance(b, _BitV2)    

class TestAttributeMessages(unittest.TestCase):
    """Test that attempt to access a v1-only attribute causes an attribute error"""
    def test_v1_only_attribute_with_v2(self):
        b = bitdotio.bitdotio("v2_5_fakeTOKENWxwNLWZvWCXi6c")
        with self.assertRaises(AttributeError) as e:
            b.list_repos()
        self.assertIn("You have configured the SDK with a v2 token, and", str(e.exception))

    """Test that attempt to access invalid attribute raises normal attribute error"""
    def test_invalid_attribute_with_v2(self):
        b = bitdotio.bitdotio("v2_5_fakeTOKENWxwNLWZvWCXi6c")
        with self.assertRaises(AttributeError) as e:
            b.fake_method()
        self.assertIn("'_BitV2' object has no attribute 'fake_method'", str(e.exception))


if __name__ == "__main__":
    unittest.main()
