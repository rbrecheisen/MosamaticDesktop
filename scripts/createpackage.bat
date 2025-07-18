@echo off

setlocal

echo Create output directory (delete if already exists)...
set OUTPUT_DIR=D:\Mosamatic\MosamaticDesktop
set OUTPUT_ZIP=D:\Mosamatic\MosamaticDesktop.zip
rmdir /s /q %OUTPUT_DIR%
mkdir %OUTPUT_DIR% 2>nul

robocopy mosamaticdesktop %OUTPUT_DIR% /E /XD __pycache__ *.dist-info .pytest_cache build dist logs /XF .gitignore CHANGELOG

copy requirements.txt %OUTPUT_DIR%
copy scripts\packagefiles\clean-python-environment.bat %OUTPUT_DIR%
copy scripts\packagefiles\clean-python-environment.ps1 %OUTPUT_DIR%
copy scripts\packagefiles\run-mosamaticdesktop.bat %OUTPUT_DIR%

powershell -Command "Compress-Archive -Path '%OUTPUT_DIR%' -DestinationPath '%OUTPUT_ZIP%' -Force"

echo Created ZIP archive: %OUTPUT_ZIP%
echo Finished

endlocal