@echo off
setlocal enabledelayedexpansion

goto :main

:print
powershell -command "Write-host %1 -ForegroundColor %2"
exit /b


:main

set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || (  echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/c cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

for /f "tokens=3 delims=\" %%a in ("!cd!") do set "username=%%a"
set "NEWUSER=C:\Users\%username%"

set "batu=%NEWUSER%\Batu"
xcopy %cd% "%batu%" /E /I /Y > nul
cd /d "%batu%"


call :print "Associating language icon" Yellow
set "ext=.batu"
set "icon=%cd%\resources\batu.ico"
assoc %ext% >nul 2>&1
if errorlevel 1 (
    assoc %ext%=filetype
    ftype filetype=%icon%
    taskkill /IM explorer.exe /F >nul
    start explorer.exe
    call :print "Icon associated with %ext% extension" Green
) else (
    call :print "An icon is already associated with %ext% extension" Yellow
)
echo.


call :print "Adding path to system environment variables" Yellow
echo %PATH% | find /i "%cd%" > nul
if errorlevel 1 (
    setx /m PATH "%PATH%;%cd%"
    call :print "%cd% added to system environment variables" Green
) else (
    call :print "%cd% already exists in system environment variables" Yellow
)
echo.


call :print "Installing VSCode extensions" Yellow
set "dest=%NEWUSER%\\.vscode\\extensions"
set "dir=batu-syntax-highlighting"
if exist "%dest%" (
    xcopy "%cd%\\%dir%" "%dest%\\%dir%" /E /I /Y > nul
    call :print "VSCode extensions installed" Green
) else (
    call :print "VSCode extensions path not found" Red
)


echo.
pause
