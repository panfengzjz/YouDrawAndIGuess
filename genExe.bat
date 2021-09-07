pyinstaller -F DrawAndGuessMain.py -w --onefile
copy dist/DrawAndGuessMain.exe .
rd /s /Q build dist