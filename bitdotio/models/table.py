# coding: utf-8

"""
    bit.io REST API

    bit.io API  # noqa: E501

    The version of the OpenAPI document: 1.0.0b
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from bitdotio.configuration import Configuration


class Table(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'url': 'str',
        'current_name': 'str',
        'description': 'str',
        'columns': 'list[str]',
        'num_records': 'int',
        'bytes': 'str',
        'repo': 'str',
        'documentation': 'str'
    }

    attribute_map = {
        'url': 'url',
        'current_name': 'current_name',
        'description': 'description',
        'columns': 'columns',
        'num_records': 'num_records',
        'bytes': 'bytes',
        'repo': 'repo',
        'documentation': 'documentation'
    }

    def __init__(self, url=None, current_name=None, description=None, columns=None, num_records=None, bytes=None, repo=None, documentation=None, local_vars_configuration=None):  # noqa: E501
        """Table - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._url = None
        self._current_name = None
        self._description = None
        self._columns = None
        self._num_records = None
        self._bytes = None
        self._repo = None
        self._documentation = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if current_name is not None:
            self.current_name = current_name
        if description is not None:
            self.description = description
        if columns is not None:
            self.columns = columns
        if num_records is not None:
            self.num_records = num_records
        if bytes is not None:
            self.bytes = bytes
        if repo is not None:
            self.repo = repo
        if documentation is not None:
            self.documentation = documentation

    @property
    def url(self):
        """Gets the url of this Table.  # noqa: E501


        :return: The url of this Table.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Table.


        :param url: The url of this Table.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def current_name(self):
        """Gets the current_name of this Table.  # noqa: E501


        :return: The current_name of this Table.  # noqa: E501
        :rtype: str
        """
        return self._current_name

    @current_name.setter
    def current_name(self, current_name):
        """Sets the current_name of this Table.


        :param current_name: The current_name of this Table.  # noqa: E501
        :type: str
        """

        self._current_name = current_name

    @property
    def description(self):
        """Gets the description of this Table.  # noqa: E501


        :return: The description of this Table.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Table.


        :param description: The description of this Table.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 400):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `400`")  # noqa: E501

        self._description = description

    @property
    def columns(self):
        """Gets the columns of this Table.  # noqa: E501


        :return: The columns of this Table.  # noqa: E501
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this Table.


        :param columns: The columns of this Table.  # noqa: E501
        :type: list[str]
        """

        self._columns = columns

    @property
    def num_records(self):
        """Gets the num_records of this Table.  # noqa: E501


        :return: The num_records of this Table.  # noqa: E501
        :rtype: int
        """
        return self._num_records

    @num_records.setter
    def num_records(self, num_records):
        """Sets the num_records of this Table.


        :param num_records: The num_records of this Table.  # noqa: E501
        :type: int
        """

        self._num_records = num_records

    @property
    def bytes(self):
        """Gets the bytes of this Table.  # noqa: E501


        :return: The bytes of this Table.  # noqa: E501
        :rtype: str
        """
        return self._bytes

    @bytes.setter
    def bytes(self, bytes):
        """Sets the bytes of this Table.


        :param bytes: The bytes of this Table.  # noqa: E501
        :type: str
        """

        self._bytes = bytes

    @property
    def repo(self):
        """Gets the repo of this Table.  # noqa: E501


        :return: The repo of this Table.  # noqa: E501
        :rtype: str
        """
        return self._repo

    @repo.setter
    def repo(self, repo):
        """Sets the repo of this Table.


        :param repo: The repo of this Table.  # noqa: E501
        :type: str
        """

        self._repo = repo

    @property
    def documentation(self):
        """Gets the documentation of this Table.  # noqa: E501


        :return: The documentation of this Table.  # noqa: E501
        :rtype: str
        """
        return self._documentation

    @documentation.setter
    def documentation(self, documentation):
        """Sets the documentation of this Table.


        :param documentation: The documentation of this Table.  # noqa: E501
        :type: str
        """

        self._documentation = documentation

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Table):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Table):
            return True

        return self.to_dict() != other.to_dict()
