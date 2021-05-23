# Stop-Curse
A small code which prevents you from being toxic in chats.
It uses tkinter, ctypes, pynput.keyboard, os.path - whatever they do
To use the project you can either:
1. Download StopCurse.py and launch it in Python
2. Download StopCurse.exe - it is exe build by Pyinstaller

After the first run StopCurse will create a short list of 'bad' words: 'idiot', 'bitch', 'cancer', 'covid', 'whore'. It is stored in 'badwords.txt'. You can edit badwords.txt manually by adding your words to your stop-list.

When you launch StopCurse you see a small window with one button. By pressing this button you activate the programm. Now when you enter the word from a stop-list you'll see the alert. You should press 'Ok' to continue ('Help' does nothing). To stop programm, press Page Up outside of its window.

How it works:
https://youtu.be/V0HDBDBlfxI
