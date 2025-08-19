@echo off

for /f "usebackq tokens=* delims=" %%a in ("requirements-win.txt") do (
    echo %%a
    poetry add %%a
)