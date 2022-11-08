# coding: utf-8
import os
import re
from setuptools import setup, find_packages  # noqa: H301


NAME = "bitdotio"
VERSIONFILE = os.path.join(NAME, "_version.py")
RE_VERSION = re.compile(r'^__version__ = "(?P<version>.+?)"$')


def get_version():
    with open(VERSIONFILE, "r") as f:
        match = RE_VERSION.match(f.read().strip())
        if match:
            return match.group("version")

        raise ValueError("Unable to parse version file")


# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["requests >= 2.28.1", "click >= 8.0.1"]

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
    version=get_version(),
    description="bit.io Python SDK and CLI",
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
    entry_points={
        "console_scripts": [
            "bit = bit.bit:main",
        ]
    },
)
