Text-to-Speech Converter
A simple Python application that converts text to speech using Google's Text-to-Speech API.
Features

User Input to Speech: Convert typed text to spoken audio
File to Speech: Convert text files to audio
Simple GUI: Easy-to-use graphical interface

Requirements

Python 3
Internet connection (required for gTTS to work)
Libraries:

gTTS (Google Text-to-Speech)
tkinter (GUI)



Installation

Clone or download this repository
git clone https://github.com/amirabdullahi/text2speech.git
cd text2speech

Install required packages:
pip install -r requirements.txt
(tkinter should be included with your Python installation)

Usage
Run the application with:
python run.py

Type text in the input field
Click "Start" to convert and play the audio
The audio will be saved as "op.mp3" and automatically played

Code Examples
Converting User Input To Speech
This GUI application allows users to type text and convert it to speech:
pythonCopyfrom gtts import gTTS
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

button = Button(text='Start', command=textToSpeech)
canvas.create_window(200, 400, window=button)

root.mainloop()

Converting a String to Speech
For simple string-to-speech conversion:
pythonCopyfrom gtts import gTTS
import os

text = "LOL this is really funny"
output = gTTS(text=text, lang='en', slow=False)
output.save("output.mp3")
os.system("start output.mp3")

Converting a Text File to Speech
For reading and converting the contents of a text file:
pythonCopyfrom gtts import gTTS
import os

text = open('demo.txt', 'r').read()
language = 'en'
output = gTTS(text=text, lang=language, slow=False)
output.save("fileoutput.mp3")
os.system("start fileoutput.mp3")
Customization

Change the language by modifying the language variable (default is 'en' for English)
Adjust speech speed with the slow parameter (set to True for slower speech)
Available languages can be found in the gTTS documentation

Troubleshooting

If you get an error about tkinter not being installed, make sure your Python installation includes tkinter
For Windows users, if audio doesn't play automatically, try changing os.system("start output.mp3") to use a specific player like os.system("explorer output.mp3")
Make sure you have an active internet connection as gTTS requires access to Google's servers
If you encounter "HTTP Error 429: Too Many Requests" or similar, wait a while before trying again as there are usage limits for the Google TTS API

File Structure
Copytext2speech/
├── run.py              # Main application file
├── requirements.txt    # Contains "gtts==2.5.4"
├── README.md           # This documentation
└── demo.txt            # Example text file (optional)
