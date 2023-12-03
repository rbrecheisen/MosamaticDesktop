#!/bin/bash

export NUITKA_CCACHE_BINARY=none
export APPNAME=MosamaticDesktop1.0

# Clean up leftovers
rm -rf main.build ${APPNAME}

# Compile Qt resources (if any)
~/.venv/RapidExplorer/bin/pyside6-rcc -o src/app/resources.py src/app/resources.qrc

# Build executable. This is the same command on MacOS or Windows. If you want to disable the console
# use the flag --disable-console on MacOS or --windows-disable-console on Windows. For MacOS or 
# Windows you do need to create different startup scripts
~/.venv/RapidExplorer/bin/python -m nuitka --standalone --include-package=pydicom --enable-plugin=pyside6 src/app/main.py

# Reorganize
mv main.dist ${APPNAME}
cp settings.ini ${APPNAME}
cp run.sh ${APPNAME}
mv ${APPNAME}/run.sh ${APPNAME}/${APPNAME}

# Build a ZIP file for the application's distribution
zip -r ${APPNAME}.zip ${APPNAME}

# Clean up
rm -rf main.build ${APPNAME}