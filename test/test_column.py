# coding: utf-8

"""
    bit.io REST API

    bit.io API  # noqa: E501

    The version of the OpenAPI document: 1.0.0b
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import bitdotio
from bitdotio.models.column import Column  # noqa: E501
from bitdotio.rest import ApiException

class TestColumn(unittest.TestCase):
    """Column unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Column
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = bitdotio.models.column.Column()  # noqa: E501
        if include_optional :
            return Column(
                url = '0', 
                current_name = '0', 
                data_type = 'BIGINT', 
                description = '0'
            )
        else :
            return Column(
        )

    def testColumn(self):
        """Test Column"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
