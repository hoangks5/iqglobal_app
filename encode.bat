@echo off
REM Đặt biến cho thư mục hiện tại
setlocal enabledelayedexpansion
set "current_dir=%cd%"

REM Duyệt qua tất cả các tệp .py trong thư mục hiện tại
for %%f in (*.py) do (
    echo Processing %%f
    REM Chạy lệnh pyarmor gen cho từng tệp .py
    pyarmor gen "%%f"
)

python -m compileall -b  .\dist\

cd /d dist
del /s /q *.py

echo Done!
pause
