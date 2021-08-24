# coding: utf-8

"""
    bit.io REST API

    bit.io API  # noqa: E501
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "bitdotio"
VERSION = "1.0.2b"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil", "psycopg2 >= 2.8.6"]

setup(
    name=NAME,
    version=VERSION,
    description="bit.io Python SDK",
    author="bit.io",
    author_email="python@bit.io",
    url="https://bit.io/",
    keywords=["bit.io", "Database", "bit.io Python SDK"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    bit.io Python SDK  # noqa: E501
    """
)
