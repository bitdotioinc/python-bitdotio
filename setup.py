# coding: utf-8

"""
    bit.io REST API

    bit.io API  # noqa: E501
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "bitdotio"
VERSION = "1.0.0b6"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
EXTRAS = {
    "psycopg2": [
        "psycopg2>=2.8.6",
    ],
    "psycopg2-binary": [
        "psycopg2-binary>=2.8.6",
    ],
}

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=NAME,
    version=VERSION,
    description="bit.io Python SDK",
    author="bit.io",
    author_email="python@bit.io",
    url="https://github.com/bitdotioinc/python-bitdotio",
    keywords=["bit.io", "Database", "bit.io Python SDK"],
    install_requires=REQUIRES,
    extras_require=EXTRAS,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Bug Tracker": "https://github.com/bitdotioinc/python-bitdotio/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
