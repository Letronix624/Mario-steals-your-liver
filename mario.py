#!/bin/python3

import tkinter
import os
import time
from threading import Thread
from pydub import AudioSegment
from pydub.playback import play as pydubplay
pydir = os.path.dirname(os.path.realpath(__file__))

NOTANOPTION = AudioSegment.from_wav(f"{pydir}/thatisnotanoption.wav")
OUCHMYEARS = AudioSegment.from_wav(f"{pydir}/ouchmyears.wav")
THREEDAYS = AudioSegment.from_wav(f"{pydir}/3days.wav")

def play(data):
    Thread(target=lambda:pydubplay(data)).start()
def ripbutton():
    play(NOTANOPTION)
    cancelbutton.place_forget()
def ok():
    root.attributes('-topmost', True)
    root.overrideredirect(True)
    mario.place_forget()
    text.place_forget()
    okbutton.place_forget()
    cancelbutton.place_forget()
    windowsize = [855, 641]
    root.geometry("855x641+"+str(1980/2-(windowsize[0]/2))[:-2]+"+"+str(1080/2-(windowsize[1]/2))[:-2])
    f1.place(x=-2, y=-1, width=859, height=645)
    l1.configure(image=kick)
    play(OUCHMYEARS)
    time.sleep(1)
    l1.configure(image=HEY)
    time.sleep(3.5)
    l1.configure(image=grab)
    time.sleep(1)
    os._exit(0)
root = tkinter.Tk()
root.geometry("400x160+"+str(1980/2-200)[:-2]+"+"+str(1080/2-80)[:-2])
root.title('')
root.configure(bg="white")
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", lambda:play(NOTANOPTION))
kick = tkinter.PhotoImage(file=f'{pydir}/kick.png', format="png")
HEY = tkinter.PhotoImage(file=f'{pydir}/hey.png', format="png")
grab = tkinter.PhotoImage(file=f'{pydir}/grab.png', format="png")
f1=tkinter.Frame(background="black")
l1 = tkinter.Label(f1)
l1.pack()
image = tkinter.PhotoImage(file=f'{pydir}/mario.png', format="png")
mario = tkinter.Label(root, image=image, bg="white")
mario.place(x=0, y=0)
text = tkinter.Label(root, text="3 Days Until Mario Steals Your Liver", background="white")
text.place(x=150, y=70, height=20)
okbutton = tkinter.Button(root, text="ok", command=lambda:Thread(target=ok).start())
cancelbutton = tkinter.Button(root, text="cancel", command=ripbutton)
okbutton.place(width=80, height=20, x=200, y=130)
cancelbutton.place(width=80, height=20, x=290, y=130)
play(THREEDAYS)
root.mainloop()
