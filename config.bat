@echo off

cd /d %~dp0

>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if %errorlevel% neq 0 (
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\temp.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\temp.vbs"
    "%temp%\temp.vbs"
    del "%temp%\temp.vbs"
    exit /b
)


powershell -command Write-Host Installing VSCode extensions -ForeGroundColor Yellow
set "dest=%USERPROFILE%\\.vscode\\extensions"
set "dir=batu-syntax-highlighting"
if EXIST "%dest%" (
    xcopy "%cd%\\%dir%" "%dest%\\%dir%" /E /I /Y > nul
    powershell -command Write-Host VSCode extensions installed -ForegroundColor Green
) else (
    powershell -command Write-Host VSCode extensions path not found -ForegroundColor Red
    goto :end
)
goto :end


powershell -command Write-Host Adding path to system environment variables -ForeGroundColor Yellow
setx /m PATH "%PATH%;%cd%"
if %errorlevel% neq 0 (
    powershell -command Write-Host Failed to add ^"%cd%^" to system environment variables -ForegroundColor Red
    goto :end
) else (
    powershell -command Write-Host ^"%cd%^" added to system environment variables -ForeGroundColor Green
)


set "ext=.batu"
set "icon=%cd%\batu.ico"
assoc %ext% >nul 2>&1
if errorlevel 1 (
    assoc %ext%=filetype
    ftype filetype=%icon%
    taskkill /IM explorer.exe /F >nul
    del /f /s /q "%userprofile%\AppData\Local\IconCache.db" >nul
    start explorer.exe
)


:end
echo.
pause