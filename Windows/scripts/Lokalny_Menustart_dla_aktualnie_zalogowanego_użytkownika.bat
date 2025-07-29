@echo off
echo ==============================
echo [1] Otworz lokalny folder Programs
echo [2] Otworz globalny folder Programs
echo ==============================
set /p choice="Wybierz opcje (1/2): "

if "%choice%"=="1" (
    explorer "%APPDATA%\Microsoft\Windows\Start Menu\Programs"
    exit
)

if "%choice%"=="2" (
    explorer "C:\ProgramData\Microsoft\Windows\Start Menu\Programs"
    exit
)

echo Nieprawidlowy wybor!
pause
