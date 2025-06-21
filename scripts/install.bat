@echo off

setlocal

rmdir /s /q .venv

poetry cache clear pypi --all
poetry update
poetry install

endlocal