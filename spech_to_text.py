import speech_recognition as sr 
import speak

def spech_to_text():
    r =  sr.Recognizer()
    with sr.Microphone() as source:
      audio = r.listen(source) # method 
      voice_data = ''
      try:
        voice_data = r.recognize_google(audio)
        return voice_data

      except sr.UnknownValueError:
             speak.speak("sorry please try again")
      except sr.RequestError:
            speak.speak('No internet connect please turn on you internet')  



