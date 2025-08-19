#!/bin/bash

cp -f pyproject.toml.macos pyproject.toml

poetry run pytest -s

read -p "Did the tests run without errors? (y/n) " CONFIRM
if [ "${CONFIRM}" == "y" ]; then
    echo "Tests ok"
else
    echo "Tests not ok"
fi

read -p "What version bump level do you want to use? [major, minor, patch (default)] " BUMP_LEVEL
if [ "${BUMP_LEVEL}" == "major" ]; then
    poetry version major
elif [ "${BUMP_LEVEL}" == "minor" ]; then
    poetry version minor
else
    poetry version patch
fi

VERSION=$(poetry version --short)
echo Deploying version ${VERSION} to PyPI...
read -p "Is this correct? (y/n) " CONFIRM
if [ ! "${CONFIRM}" == "y" ]; then
    echo "Aborting deployment..."
    exit 1
fi

TOKEN=$(cat "/Users/ralph/Library/CloudStorage/GoogleDrive-ralph.brecheisen@gmail.com/My Drive/data/ApiKeysAndPasswordFiles/pypi-token.txt")

poetry build
poetry publish --username __token__ --password ${TOKEN}

cp -f pyproject.toml pyproject.toml.macos

git tag v${VERSION}
git push origin v${VERSION}
git add -A
git commit -m "Saving pyproject.toml"
git push