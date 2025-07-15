@echo off

setlocal

python -m pip install %1 -r requirements-windows.txt

endlocal