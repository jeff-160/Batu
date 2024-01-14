@echo off

goto :main

:print
powershell -command "Write-host %1 -ForegroundColor %2"
exit /b


:main

cd /d %~dp0

>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
if %errorlevel% neq 0 (
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\temp.vbs"
    echo UAC.ShellExecute "%~s0", "", "", "runas", 1 >> "%temp%\temp.vbs"
    "%temp%\temp.vbs"
    del "%temp%\temp.vbs"
    exit /b
)


set "batu=%USERPROFILE%\\Batu"
xcopy %cd% "%batu%" /E /I /Y > nul
cd /d "%batu%"


call :print "Installing VSCode extensions" Yellow
set "dest=%USERPROFILE%\\.vscode\\extensions"
set "dir=batu-syntax-highlighting"
if exist "%dest%" (
    xcopy "%cd%\\%dir%" "%dest%\\%dir%" /E /I /Y > nul
    call :print "VSCode extensions installed" Green
) else (
    call :print "VSCode extensions path not found" Red
    goto :end
)
echo.


call :print "Adding path to system environment variables" Yellow
setx /m PATH "%PATH%;%cd%"
if %errorlevel% neq 0 (
    call :print "Failed to add %cd% to system environment variables" Red
    goto :end
) else (
    call :print "%cd% added to system environment variables" Green
)
echo.
goto :end


call :print "Associating language icon" Yellow
set "ext=.batu"
set "icon=%cd%\resources\batu.ico"
assoc %ext% >nul 2>&1
if errorlevel 1 (
    assoc %ext%=filetype
    ftype filetype=%icon%
    taskkill /IM explorer.exe /F >nul
    del /f /s /q "%userprofile%\AppData\Local\IconCache.db" >nul
    start explorer.exe

    call :print "Icon associated with .batu extension"
) else (
    call :print "Failed to associate icon"
)


:end
echo.
pause
