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