@echo off

setlocal

rmdir /s /q .venv

del poetry.lock

poetry cache clear pypi --all
poetry update
poetry install

poetry show mosamatic-cli

endlocal