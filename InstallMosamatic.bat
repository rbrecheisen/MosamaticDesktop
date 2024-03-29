@echo off
setlocal EnableDelayedExpansion

@REM https://chat.openai.com/c/143bf330-901c-46ea-9115-03b450fdd07d
@REM Also install Python 3 if needed

set VENV_DIR=%USERPROFILE%\.mosamatic\MosamaticDesktop

echo "Creating virtual environment..."
if not exist "%USERPROFILE%\.mosamatic\" mkdir "%USERPROFILE%\.mosamatic"
cd /d "%USERPROFILE%\.mosamatic"
if not exist "%VENV_DIR%" (
    python -m venv "%VENV_DIR%"
)

echo "Installing requirements..."
call "%VENV_DIR%\Scripts\activate"
%USERPROFILE%\.mosamatic\MosamaticDesktop\bin\pip install --upgrade pip
%USERPROFILE%\.mosamatic\MosamaticDesktop\bin\pip install mosamaticdesktop
call "%VENV_DIR%\Scripts\deactivate.bat"

echo "Installing executable..."
copy %USERPROFILE%\.mosamatic\MosamaticDesktop\Scripts\mosamatic-desktop.exe C:\Windows

echo "Creating desktop shortcut for executable..."
SET ExePath=C:\Windows\mosmatic-desktop.exe
SET ShortcutName=Mosmatic Desktop

FOR /F "tokens=*" %%I IN ('reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders" /v Desktop') DO SET DesktopPath=%%I
SET DesktopPath=%DesktopPath:*REG_SZ=%
SET DesktopPath=%DesktopPath:~1%

SET VBSFile=%temp%\tempshortcut.vbs
(
echo Set oWS = WScript.CreateObject("WScript.Shell"^)
echo sLinkFile = "%DesktopPath%\%ShortcutName%.lnk"
echo Set oLink = oWS.CreateShortcut(sLinkFile^)
echo oLink.TargetPath = "%ExePath%"
echo oLink.Save
) > !VBSFile!

cscript //nologo "%VBSFile%"

del "%VBSFile%"

echo "Installation finished."
echo "You can now run Mosamatic Desktop by double-clicking the shortcut on your desktop."

endlocal
