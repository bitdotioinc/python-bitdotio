#!/bin/bash
set -exu -o pipefail
set +e
rm -rf dist/*
rm -rf build/*
rm -rf bitdotio.egg-info
set -e
pip install wheel bumpversion twine
python setup.py sdist bdist_wheel
python -m twine check dist/*
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
