@echo off
set /p VERSION=<src\mosamaticdesktop\resources\VERSION
call python -m pip install -r requirements.txt
call python -m briefcase dev