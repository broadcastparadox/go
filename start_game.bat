@echo off
cd /d %~dp0
start "Go Backend" cmd /k "python backend\main.py"
TIMEOUT /T 2 >nul
start http://localhost:5000/ 