@echo off

setlocal

FOR /F %%v IN ('poetry version --short') DO SET VERSION=%%v
echo %VERSION% > mosamaticdesktop\resources\VERSION

poetry run mosamaticdesktop

endlocal