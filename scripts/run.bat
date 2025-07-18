@echo off

setlocal

set /p VERSION=<mosamaticdesktop\src\mosamaticdesktop\resources\VERSION

set START_DIR=%CD%

set /p BRIEFCASE=<which briefcase

if /I "%~1"=="" (

    cd mosamaticdesktop
    call briefcase dev

) else if /I "%~1"=="--test" (

    cd mosamaticdesktop
    call briefcase dev --test

) else if /I "%~1"=="--exe" (

    cd mosamaticdesktop
    call briefcase run

) else if /I "%~1"=="--build" (

    rmdir /s /q mosamaticdesktop\build
    call python scripts\python\updatetomlversion.py %VERSION%
    call python scripts\python\updatetomlrequirements.py windows
    cd mosamaticdesktop
    call briefcase create
    call briefcase build

) else if /I "%~1"=="--package" (

    rmdir /s /q mosamaticdesktop\dist
    @rem Hack: packaging fails because of long TensorFlow header file paths
    rmdir /s /q "mosamaticdesktop\build\mosamaticdesktop\windows\app\src\app_packages\tensorflow\include"
    cd mosamaticdesktop
    call briefcase package --adhoc-sign
    
)

cd %START_DIR%


endlocal