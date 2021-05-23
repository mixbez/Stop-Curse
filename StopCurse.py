import tkinter as tk
import ctypes
from pynput import keyboard
import os.path
from os import path

badwords = []
if (path.exists("badwords.txt")):
    with open("badwords.txt", "r") as text_file:
        lines = text_file.readlines()
        for line in lines:
            words = line.split(",")
            for word in words:
                badwords.append(word)
else:
    badwords = ['bitch', 'cancer','idiot','whore','covid']
    with open("badwords.txt", "w") as text_file:
        for i in range (len(badwords)-1):
            text_file.write(badwords[i] + ",")
        text_file.write(badwords[-1])
    print ("I created a file")
lastkeys = []
max_bad_len = 0
for element in badwords:
    max_bad_len = max(max_bad_len, len(element))
def on_press(key):
    if key == keyboard.Key.page_up:
        return False  # stop listener
    if key == keyboard.Key.backspace:
        if (len(lastkeys) > 0):
            lastkeys.pop()
    try:
        k = key.char  # single-char keys
        #print (ord(k))
        if (ord(k) >= 65 and ord(k) < 123):
            #print (ord(k))
            lastkeys.append(k)
            if len(lastkeys) > max_bad_len:
                lastkeys.pop(0)
            words = createWords(listToString(lastkeys))
            checkCurses(badwords, words)
    except:
        i = 1  # other keys
def checkCurses (badwords, words):
    for word in words:
        if word in badwords:
            alert = 'You typed ' + word[:1].upper() + '-word. Are you sure you want to send it to chat?'
            print (alert)
            ctypes.windll.user32.MessageBoxW(0, alert, "Curse Alert")
def createWords (main_word):
    all_words = []
    l = len(main_word)
    for i in range (1, l + 1):
        all_words.append(main_word[-i:].lower())
    return all_words

def listToString (lst):
    st = ""
    for element in lst:
        st += element
    return st

def start():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

button1 = tk.Button(text='Start (To turn off press Page Up!)', command=start, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()