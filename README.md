Text-to-Speech Converter

A simple Python application that converts text to speech using Google's Text-to-Speech API.
Features

- User Input to Speech: Convert typed text to spoken audio
- File to Speech: Convert text files to audio
- Simple GUI: Easy-to-use graphical interface

Requirements

- Python 
- Internet connection (required for gTTS to work)
- Libraries:
  - `gTTS` (Google Text-to-Speech)
  - `tkinter` (GUI)

Installation

1. Clone or download this repository
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
   (tkinter should be included with your Python installation)

Run the application with:
```
python run.py
```

1. Type text in the input field
2. Click "Start" to convert and play the audio
3. The audio will be saved as "op.mp3" and automatically played

 Using Code Snippets

The repository also includes example code for:

- Converting a string to speech:
  ```python
  from gtts import gTTS
  import os
  
  text = "LOL this is really funny"
  output = gTTS(text=text, lang='en', slow=False)
  output.save("output.mp3")
  os.system("start output.mp3")
  ```

- Converting a text file to speech:
  ```python
  from gtts import gTTS
  import os
  
  text = open('demo.txt', 'r').read()
  language = 'en'
  output = gTTS(text=text, lang=language, slow=False)
  output.save("fileoutput.mp3")
  os.system("start fileoutput.mp3")
  ```
-Converting User Input To Speech
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
 Customization

- Change the language by modifying the `language` variable (default is 'en' for English)
- Adjust speech speed with the `slow` parameter (set to `True` for slower speech)
- Available languages can be found in the [gTTS documentation](https://gtts.readthedocs.io/en/latest/)
