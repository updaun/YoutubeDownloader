@echo off

:start
cls
echo starting install pytube library.  
echo.
pip install -U pytube
python ./src/GUI.py
exit