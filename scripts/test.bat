@echo off

setlocal

poetry run pytest -p no:warnings

endlocal