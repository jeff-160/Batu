@echo off

cd /d %~dp0

>nul 2>&1 net session
if %errorlevel% neq 0 (
    powershell -command Write-Host This script requires administrator privileges -ForegroundColor Red
    goto :end
)

powershell -command Write-Host Adding path to system environment variables -ForeGroundColor Yellow
setx /m PATH "%PATH%;%cd%"
if %errorlevel% neq 0 (
    powershell -command Write-Host Failed to add ^"%cd%^" to system environment variables -ForegroundColor Red
    goto :end
) else (
    powershell -command Write-Host ^"%cd%^" added to system environment variables -ForeGroundColor Green
)

@REM set "ext=.batu"
@REM set "icon=%cd%\batu.ico"

@REM assoc %ext% >nul 2>&1
@REM if errorlevel 1 (
@REM     assoc %ext%=filetype
@REM     ftype filetype=%icon%

@REM     taskkill /IM explorer.exe /F >nul
@REM     del /f /s /q "%userprofile%\AppData\Local\IconCache.db" >nul
@REM     start explorer.exe
@REM )

:end
echo.
pause