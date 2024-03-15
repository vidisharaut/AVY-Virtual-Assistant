import datetime
import speak
import webbrowser
import weather
import os
import pyautogui
import time
import wikipedia
import cv2
import requests
import speech_recognition as sr
import keyboard
from PIL import Image
from tkinter import filedialog
from time import sleep
from config import key
import requests

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


def chat1(chat):
    messages = []
    system_message = "You are an AI Virtual Assistant Project created by Vidisha, Yakuta, Akshada and guided by Prajakta Ma'am, your name is AVY. You respond like humans."
    message = { "role" : "user", "parts" : [{"text":'give me the answer of ' + system_message + " " + chat +  'in one sentence' }]}
    messages.append(message)
    data = {'contents' : messages}
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url, json=data)
    t1 = response.json()
    t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    t3 = t2.replace('*', '')
    return t3

gender = 'Female'
if(gender == 'Male'):
    person = 'Sir'
elif(gender == 'Female'):
    person = "Ma'am"

def Action(send) :   
  
    data_btn  = send.lower()

#1
    if "time now" in data_btn:       #Execution Successful
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 
#2
    elif "how are you" in  data_btn :       #Execution Successful
        speak.speak("I am doing great these days {}".format(person)) 
        return "I am doing great these days {}".format(person)
#3
    elif "thanku" in data_btn or "thank" in data_btn:       #Execution Successful
        speak.speak("its my pleasure Ma'am to stay with you")
        return "its my pleasure sir to stay with you" 
#4
    elif "play music" in data_btn or "song" in data_btn:       #Execution Successful
        webbrowser.open("https://gaana.com/")   
        speak.speak("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"
#5
    elif 'open google' in data_btn:      #Execution Successful
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("Opening Google")  
        return "Opening Google"
#6
    elif "open youtube" in  data_btn:       #Execution Successful
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("Opening YouTube") 
        return "Opening YouTube"   
#7 
    # elif 'close youtube' in data_btn:       #Execution Unsuccessful
    #     os.system("taskkill /f /im msedge.exe")
    #     speak.speak("Opening YouTube") 
    #     return "Opening YouTube"  
#8   
    elif 'weather' in data_btn :       #Execution Successful
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans
#9
    elif 'music from my laptop' in data_btn:        #Not Executed
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..."       
 #10   
    #Vidisha's changes: 
    elif "shutdown" in data_btn:       #Execution Successful
        speak.speak("Shuting Down")
        os.system("shutdown /s /t 5")
        return "ok sir" 
#11
    elif "lock the system" in data_btn:       #Execution Successful
        speak.speak("Locking the system...")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        return "System Locked" 
#12
    elif "restart the system" in data_btn:       #Not Executed
        speak.speak("Restarting the system...")
        os.system("shutdown /r /t 5")
        return "Restarting the system..." 
#13
    elif "open command" in data_btn:       #Execution Successful
        speak.speak("Opening Command Prompt")
        os.system("start cmd")
        return "Opening Command Prompt"
#14
    elif "close command prompt" in data_btn:       #Execution Successful
        text = "Closing Command Prompt"
        speak.speak(text)
        os.system("taskkill /f /im cmd.exe")
        return text
#15
    # elif "open notepad" in data_btn:       #Execution Successful
    #     npath = r"C:\Windows\System32\notepad.exe" 
    #     text = "Opening Notepad"
    #     speak.speak(text)
    #     os.startfile(npath)
    #     return text
#16
    elif "close notepad" in data_btn:       #Execution Successful
        text = "Closing NotePad"
        speak.speak(text)
        os.system("taskkill /f /im notepad.exe")
        return text
#17
    elif "open microsoft word" in data_btn:       #Execution Successful
        text = "Opening Microsoft Word"
        speak.speak(text)
        npath = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
        os.startfile(npath)
        return text
#18
    elif "close microsoft word" in data_btn:       #Execution Successful
        text1 = "Closing Microsoft Word"
        speak.speak(text1)
        os.system("wmic process where \"name='winword.exe'\" delete")
        return text1
#19
    elif "open microsoft excel" in data_btn:       #Execution Successful
        text = "Opening Microsoft Excel"
        speak.speak(text)
        npath = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
        os.startfile(npath)
        return text
#20
    elif "close microsoft excel" in data_btn:       #Execution Successful
        text1 = "Closing microsoft excel"
        speak.speak(text1)
        os.system("taskkill /f /im excel.exe")
        return text1
#21
    elif "open microsoft powerpoint" in data_btn:       #Execution Successful
        text = "Opening Microsoft Powerpoint"
        speak.speak(text)
        npath = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
        os.startfile(npath)
        return text
#22
    elif "close microsoft powerpoint" in data_btn:       #Execution Successful
        text1 = "Closing Powerpoint"
        speak.speak(text1)
        os.system("taskkill /f /im powerpnt.exe")
        return text1
#23
    elif 'open chrome' in data_btn:       #Execution Successful
        text = "Opening Google Chrome"
        speak.speak(text)
        npath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        os.startfile(npath)
        return text
#24
    elif 'maximize this window' in data_btn:       #Execution Successful
        text = 'Maximizing this window'
        speak.speak(text)
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('x')
        return text
#25
    elif 'google search' in data_btn:       #Execution Successful but need to clear history
        data_btn = data_btn.replace("google search", "")
        pyautogui.hotkey('alt', 'd')
        pyautogui.write(f"{data_btn}", 0.1)
        pyautogui.press('enter')
#26
    elif 'open new window' in data_btn:       #Execution Successful 
        pyautogui.hotkey('ctrl', 'n')

#27
    elif 'open incognito window' in data_btn:       #Execution Successful
        pyautogui.hotkey('ctrl', 'shift', 'n')
#28
    elif 'minimise this window' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('n')
#29
    elif 'open history' in data_btn:       #Execution Successful
        pyautogui.hotkey('ctrl', 'h')
#30
    elif 'open downloads' in data_btn:       #Execution Successful
        pyautogui.hotkey('ctrl', 'j')
#31
    elif 'previous tab' in data_btn:       #Execution Successful
        pyautogui.hotkey('ctrl', 'shift', 'tab')
    elif 'next tab' in data_btn:       #Execution Successful
        pyautogui.hotkey('ctrl', 'tab')
    elif 'close tab' in data_btn:       #Execution Successful
        pyautogui.hotkey('ctrl', 'w')
    elif 'close window' in data_btn:       #Execution Successful
        pyautogui.hotkey('ctrl', 'shift', 'w')
    elif 'clear browsing history' in data_btn:       #Execution Successful 
        pyautogui.hotkey('ctrl', 'shift', 'delete')
    elif 'close chrome' in data_btn:       #Execution Successful
        os.system("taskkill /f /im chrome.exe")
    elif "take screenshot" in data_btn:
            speak.speak("Sir, Please tell me the name for the screenshot file")
            name = takeCommand()
            print(name)
            speak.speak("Taking Screenshot...!")
            time.sleep(2)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak.speak("ScreenShot Saved...!")
            return "ScreenShot Saved...!"
    elif 'wikipedia' in data_btn:       #Execution Successful       --incomplete Work
        speak.speak('Searching Wikipedia...')
        results = wikipedia.summary(data_btn, sentences=2)
        speak.speak("According to Wikipedia")
        speak.speak(results)
        return results
    elif "open camera" in data_btn:       #Execution Successful
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(50)
            if k==27:
                break;
        cap.release()
        cv2.destroyAllWndows()
    elif "turn the volume up" in data_btn:       #Execution Successful
        pyautogui.press("volumeup")
    elif "turn the volume down" in data_btn:       #Execution Successful
        pyautogui.press("volumedown")
    elif "mute" in data_btn:       #Execution Successful
        pyautogui.press("volumemute")
    elif "stop" in data_btn:
        exit()

    elif "open" in data_btn:
        Nameoftheapp = data_btn.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)  
        return True

    else :
        try:
            res = chat1(data_btn)
            speak.speak(res);
            return res;
        except Exception as e:
            speak.speak( "i'm unable to understand!")
            return "i'm unable to understand!" 
        

