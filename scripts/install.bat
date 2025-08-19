@echo off

setlocal

del poetry.lock

copy /Y pyproject.toml.windows pyproject.toml

python -m pip install -r requirements-win.txt
poetry config virtualenvs.create false --local

@REM poetry cache clear pypi --all
@REM poetry update
poetry install

endlocal