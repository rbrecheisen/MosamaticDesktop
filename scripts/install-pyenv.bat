@ECHO off

setlocal

powershell -ExecutionPolicy Bypass -NoProfile -File "%~dp0install-pyenv-win.ps1"

endlocal