@echo off
setlocal enabledelayedexpansions
echo [1/2] Running build...
python build.py
if errorlevel 1 (
    echo [!] build failed.
    pause
    exit /b 1
)
echo [2/2] Cleaning up temporary files...
rmdir /s /q build 2>nul
del /f /q loader-o.py 2>nul
del /f /q loader-o.spec 2>nul
del /f /q blank.aes 2>nul
del /f /q noconsole 2>nul
del /f /q pumpStub 2>nul
del /f /q bound.blank 2>nul

echo ==========================================
echo Build complete!
echo Final EXE is in the current directory.
echo ==========================================
pause