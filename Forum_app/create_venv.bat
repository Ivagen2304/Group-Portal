@echo off
echo Creating venv...
py -m venv venv
echo Venv created.
echo Downloading requirements...
venv\Scripts\pip install -r requirements.txt
echo Requirements installed.
pause