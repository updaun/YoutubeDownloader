@echo off

:start
cls
echo starting install pytube library.  
echo.
pip install -r requirements.txt
python ./src/GUI.py
exit