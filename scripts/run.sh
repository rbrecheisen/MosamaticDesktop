#!/bin/bash

VERSION=$(cat poetry version --short)
echo ${VERSION} > mosamaticdesktop/resources/VERSION

poetry run mosamaticdesktop