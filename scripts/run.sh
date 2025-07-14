#!/bin/bash

VERSION=$(cat mosamaticdesktop/src/mosamaticdesktop/resources/VERSION)

if [ "${1}" == "" ]; then

    cd mosamaticdesktop
    briefcase dev

elif [ "${1}" == "--test" ]; then

    cd mosamaticdesktop
    briefcase dev --test

elif [ "${1}" == "--exe" ]; then

    cd mosamaticdesktop
    briefcase run

elif [ "${1}" == "--build" ]; then

    rm -rf mosamaticdesktop/build
    python scripts/python/updatetomlversion.py ${VERSION}
    python scripts/python/updatetomlrequirements.py macos
    cd mosamaticdesktop
    briefcase create
    briefcase build

elif [ "${1}" == "--package" ]; then

    cd mosamaticdesktop
    briefcase package --adhoc-sign
fi