pyinstaller -F DrawAndGuessMain.py -w --onefile -i cover.ico
copy dist/DrawAndGuessMain.exe .
rd /s /Q build dist