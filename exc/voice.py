import pyttsx3
import threading
txt = pyttsx3.init()
def say(text):
    voices = txt.getProperty('voices')
    txt.setProperty('voice', voices[1].id)
    txt.setProperty('rate', 320)
    txt.say(text)
    txt.runAndWait()

def new(counter,stage,prevstage):
    if stage != prevstage:
        text = f"{counter} {stage}"
        threading.Thread(target=say, args=(text,)).start()

def voicespeech(counter,stage):
    text = f"{counter} {stage}"
    threading.Thread(target=say, args=(text,)).start()