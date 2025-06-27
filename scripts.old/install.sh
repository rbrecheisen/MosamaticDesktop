#!/bin/bash

rm -rf ./.venv

rm poetry.lock

poetry cache clear pypi --all
poetry update
poetry install

poetry show mosamatic-cli