# pip install pyttsx3

import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  
    rate = engine.getProperty('rate')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', rate-60)
    engine.say(text)
    engine.runAndWait()

