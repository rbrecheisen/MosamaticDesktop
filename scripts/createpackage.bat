@echo off

setlocal

set /p VERSION=<mosamaticdesktop\src\mosamaticdesktop\resources\VERSION

set /p CONFIRM="Creating package for version %VERSION%. Is this the correct version? (y/n) "
if /I NOT "%CONFIRM%"=="y" (
    echo Aborting package creation
    exit /b 1
)

echo Create output directory (delete if already exists)...
set OUTPUT_DIR=D:\Mosamatic\MosamaticDesktop
set OUTPUT_ZIP=D:\Mosamatic\MosamaticDesktop-%VERSION%.zip
rmdir /s /q %OUTPUT_DIR%
mkdir %OUTPUT_DIR% 2>nul
mkdir %OUTPUT_DIR%\model 2>nul

@REM Source code
robocopy mosamaticdesktop %OUTPUT_DIR% /E /XD __pycache__ *.dist-info .pytest_cache build dist logs tests /XF .gitignore CHANGELOG

@REM Scripts
copy requirements.txt %OUTPUT_DIR%
copy scripts\packagefiles\clean-python-environment.bat %OUTPUT_DIR%
copy scripts\packagefiles\clean-python-environment.ps1 %OUTPUT_DIR%
copy scripts\packagefiles\run-mosamaticdesktop.bat %OUTPUT_DIR%

@REM TensorFlow model
copy "G:\My Drive\data\Mosamatic\models\tensorflow\L3\1.0\model-1.0.zip" %OUTPUT_DIR%\model
copy "G:\My Drive\data\Mosamatic\models\tensorflow\L3\1.0\contour_model-1.0.zip" %OUTPUT_DIR%\model
copy "G:\My Drive\data\Mosamatic\models\tensorflow\L3\1.0\params-1.0.json" %OUTPUT_DIR%\model

powershell -Command "Compress-Archive -Path '%OUTPUT_DIR%' -DestinationPath '%OUTPUT_ZIP%' -Force"

echo Created ZIP archive: %OUTPUT_ZIP%
echo Finished

endlocal