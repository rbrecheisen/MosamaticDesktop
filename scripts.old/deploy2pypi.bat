@echo off

setlocal

poetry run pytest

set /p CONFIRM="Did the tests run without errors? (y/n) "
if /I NOT "%CONFIRM%"=="y" (
    echo Aborting deployment
    exit /b 1
)

set /p BUMP_LEVEL="What version bump level do you want to use? [major, minor, patch (default)] "
if /I "%BUMP_LEVEL%"=="major" (
    poetry version major
) else if /I "%BUMP_LEVEL%"=="minor" (
    poetry version minor
) else (
    poetry version patch
)

FOR /F %%v IN ('poetry version --short') DO SET VERSION=%%v
echo Deploying version %VERSION% to PyPI...
set /p CONFIRM="Is this correct? (y/n) "
if /I NOT "%CONFIRM%"=="y" (
    echo Aborting deployment
    exit /b 1
)

echo %VERSION% > mosamaticdesktop\resources\VERSION

set /p TOKEN=<"G:\My Drive\data\ApiKeysAndPasswordFiles\pypi-token.txt"

poetry build
poetry publish --username __token__ --password %TOKEN%

git tag v%VERSION%
git push origin v%VERSION%
git add -A
git commit -m "Saving pyproject.toml"
git push

endlocal