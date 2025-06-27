@echo off

setlocal

pip install --upgrade pip
pip install -r requirements.txt
cd mosamaticdesktop
call briefcase create

endlocal