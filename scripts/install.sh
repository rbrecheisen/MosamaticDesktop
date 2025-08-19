#!/bin/bash

rm -rf ./.venv

rm poetry.lock

cp -f pyproject.toml.macos pyproject.toml

python -m pip install -r requirements-macos.txt
poetry config virtualenvs.create false --local

# poetry cache clear pypi --all
# poetry update
poetry install