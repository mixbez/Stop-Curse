import tkinter as tk
import ctypes
from pynput import keyboard
from os import path
global max_bad_len

badwords = []

def ruToEng(word):
    symbols = (u"абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz",
               u"f,dult`;pbqrkvyjghcnea[wxio]sm'.zаисвуапршолдьтщзйкыегмцчня")

    tr = {ord(a): ord(b) for a, b in zip(*symbols)}
    return word.translate(tr)

def newLength():
    if len(badwords) == 0:
        return 0
    l = 0
    for element in badwords:
        l = max(l, len(element))
    return l
def writeWords():
    global max_bad_len
    with open("badwords.txt", "w") as text_file:
        for i in range (len(badwords)-1):
            text_file.write(badwords[i] + ",")
        text_file.write(badwords[-1])
    max_bad_len = newLength()

if (path.exists("badwords.txt")):
    with open("badwords.txt", "r") as text_file:
        lines = text_file.readlines()
        for line in lines:
            words = line.split(",")
            for word in words:
                badwords.append(word)
else:
    badwords = ['bitch', 'cancer','idiot','whore','covid']
    max_bad_len = writeWords()
lastkeys = []
max_bad_len = newLength()
def on_press(key):
    if key == keyboard.Key.page_up:
        return False  # stop listener
    if key == keyboard.Key.backspace:
        if (len(lastkeys) > 0):
            lastkeys.pop()
    try:
        k = key.char
        if ((ord(k) >= 65 and ord(k) < 123) or (ord(k) >= 1040 and ord(k) < 1104)):
            print (ord(k))
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
        tr = ruToEng(word)
        # print (word, tr)  bitch чмо xvj bitch ишеср

        if tr in badwords:
            alert = 'You typed ' + tr[:1].upper() + '-word. Are you sure you want to send it to chat?'
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

def addWord():
    x1 = entry1.get()
    if (x1 != ""):
        badwords.append(x1)
    writeWords()

root = tk.Tk()
root.title('Stop Curse')
#bitch
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

button1 = tk.Button(text='Start (To turn off press Page Up!)', command=start, bg='brown', fg='white')
canvas1.create_window(150, 150, window=button1)

entry1 = tk.Entry (root)
canvas1.create_window(125, 100, window=entry1)

button2 = tk.Button(text ='Add word', command = addWord, bg = 'green', fg = 'black')
canvas1.create_window(175, 100, window=button2)

root.mainloop()