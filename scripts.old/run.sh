#!/bin/bash

VERSION=$(poetry version --short)
echo ${VERSION} > mosamaticdesktop/resources/VERSION

poetry run mosamaticdesktop