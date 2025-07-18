Invoke-WebRequest -UseBasicParsing https://pyenv.run | Invoke-Expression

[System.Environment]::SetEnvironmentVariable("PYENV", "%USERPROFILE%\.pyenv\pyenv-win", "User")

$oldPath = [System.Environment]::GetEnvironmentVariable("Path", "User")
$newEntry = "%PYENV%\bin;%PYENV%\shims"
if (-not ($oldPath -split ";" | Where-Object { $_ -eq $newEntry })) {
    $newPath = "$oldPath;$newEntry"
    [System.Environment]::SetEnvironmentVariable("Path", $newPath, "User")
}