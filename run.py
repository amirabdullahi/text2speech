from gtts import gTTS
import os
from tkinter import *


root = Tk()
canvas = Canvas(root, width=500, height=500)
canvas.pack()


def textToSpeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save("op.mp3")
    os.system('start op.mp3')

entry = Entry(root, width=30)
canvas.create_window(200, 350, window=entry)

button = Button(text='Start',command=textToSpeech)
canvas.create_window(200, 400, window=button)

root.mainloop()

# text = "LOL this is really funny"
# output=gTTS(text=text,lang='en', slow=False)

# output.save("output.mp3")
# os.system("start output.mp3")

# text = open('demo.txt', 'r').read()
# language = 'en'
# output=gTTS(text=text,lang=language, slow=False)
# output.save("fileoutput.mp3")
# os.system("start fileoutput.mp3")