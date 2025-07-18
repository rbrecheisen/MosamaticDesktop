@echo off

setlocal

echo Create output directory (delete if already exists)...
set OUTPUT_DIR=D:\Mosamatic\MosamaticDesktop
rmdir /s /q %OUTPUT_DIR%
mkdir %OUTPUT_DIR% 2>nul

robocopy mosamaticdesktop %OUTPUT_DIR% /E /XD __pycache__ *.dist-info .pytest_cache build dist logs /XF .gitignore CHANGELOG

copy requirements.txt %OUTPUT_DIR%
copy scripts\install-pyenv-win.ps1 %OUTPUT_DIR%
copy scripts\install-pyenv.bat %OUTPUT_DIR%
copy scripts\install-mosamaticdesktop.bat %OUTPUT_DIR%
copy scripts\run.bat %OUTPUT_DIR%

cd %OUTPUT_DIR%
dir

echo Finished

endlocal