import datetime
import speak
import webbrowser
import weather
import os
import pyautogui
import time
import wikipedia
import requests
import speech_recognition as sr
import keyboard
from keyboard import press
from keyboard import press_and_release
from PIL import Image
from tkinter import filedialog
from time import sleep
from config import key
import requests
import ctypes
import gspread
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json
import pyttsx3
import threading
import NewsRead

def get_google_sheet():
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = Credentials.from_service_account_file('credentials.json', scopes=scope)
    client = gspread.authorize(creds)
    sheet_id = '19KSBOcqj-F3rPvMqkw4EQe5xA5UI0OuIXrGwRleSSyk'
    sheet = client.open_by_key(sheet_id).sheet1
    return sheet


def add_data_to_sheet(data):
    try:
        sheet = get_google_sheet()
        sheet.append_row(data)
        return "Data added successfully to Google Sheets"
    except Exception as e:
        return f"Error adding data to Google Sheets: {str(e)}"


def add_data_to_sheet_speech():
    try:
        # Ask the user for data related to each column
        prompts = ["What should be the date?", "What is your D. S. A. Topic?",
                   "How many D. S. A. questions should be solved?",
                   "How many DSA questions have you solved?",
                   "What is the priority level for DSA?",
                   "What is your study subject?",
                   "Which module u are studying?",
                   "What is the priority level for that subject?",
                   "What is the status of your study?"]

        data_to_add = []
        for prompt in prompts:
            speak.speak(prompt)
            user_input = takeCommand()
            data_to_add.append(user_input)

        response = add_data_to_sheet(data_to_add)
        speak.speak(response)
        return response
    except Exception as e:
        return f"Error adding data to Google Sheets: {str(e)}"
        
def show_tableau_dashboard():
    # Replace 'YOUR_TABLEAU_DASHBOARD_URL' with the actual URL of your Tableau dashboard
    tableau_dashboard_url = 'https://public.tableau.com/views/TodoListTask/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link'
    webbrowser.open(tableau_dashboard_url)


def square_spiral():
    pyautogui.click() 
    # initialising a variable distance 
    distance = 200
  
  
    while (distance): 
        # moves the cursor to the right 
        pyautogui.dragRel(distance, 0, duration=0.2) 
        distance = distance - 20
        # move the cursor down 
        pyautogui.dragRel(0, distance, duration=0.2) 
        # move the cursor to the left 
        pyautogui.dragRel(-distance, 0, duration=0.2) 
        distance = distance - 20
        # move the cursor up 
        pyautogui.dragRel(0, -distance, duration=0.2)

def drawSquare():

    # Make a delay of 2 sec 
    time.sleep(2) 
    pyautogui.click() 
    l = 200  # initialising variable l 
    a = 4  # initialising variable a 
  
    pyautogui.dragRel(200, 0, 0.1) 
    a -= 1
    pyautogui.dragRel(0, 200, 0.1) 
    a -= 1
    pyautogui.dragRel(-200, 0, 0.1) 
    a -= 1
    pyautogui.dragRel(0, -200, 0.1) 
    a -= 1

def drawHouse():
    time.sleep(5) 
    pyautogui.click()  # using .click() method to click 
    l = 200
    a = 4
    x, y = pyautogui.position() 
  
    # making a square first 
  
    pyautogui.dragRel(200, 0, 0.2) 
    x1, y1 = pyautogui.position() 
    a -= 1
    pyautogui.dragRel(0, 200, 0.2) 
    a -= 1
    pyautogui.dragRel(-200, 0, 0.2) 
    a -= 1
    pyautogui.dragRel(0, -200, 0.2) 
    a -= 1
  
    # making a triangle over the square 
    pyautogui.click(x, y) 
    pyautogui.dragRel(100, -100, 0.2) 
    pyautogui.click(x1, y1) 
    pyautogui.dragRel(-100, -100, 0.2) 
  
    # making rest of the body of the hut 
    pyautogui.dragRel(350, 0, 0.2) 
    pyautogui.dragRel(0, 300, 0.2) 
    pyautogui.dragRel(-290, 0, 0.2) 
    pyautogui.click(x1, y1) 
    pyautogui.dragRel(250, 0, 0.2) 

def move_cursor():
    height = 1920
    width = 1080
    pyautogui.moveTo(height / 2, width / 2)



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
    elif 'weather' in data_btn :       #Execution Successful
       ans   = weather.Weather()
       speak.speak(ans) 
       return ans
#8
    # elif 'music from my laptop' in data_btn:        #Not Executed
    #     url = 'D:\\music' 
    #     songs = os.listdir(url)
    #     os.startfile(os.path.join(url, songs[0]))
    #     speak.speak("songs playing...")
    #     return "songs playing..."       
 #9   
    #Vidisha's changes: 
    elif "shutdown" in data_btn:       #Execution Successful
        speak.speak("Shuting Down")
        os.system("shutdown /s /t 5")
        return "ok sir" 
#10
    # elif "lock the system" in data_btn:       #Execution Successful
    #     speak.speak("Locking the system...")
    #     os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    #     return "System Locked" 
    elif "lock the system" in data_btn:
        speak.speak("Locking the system...")
        ctypes.windll.user32.LockWorkStation()
        return "System Locked"
#11
    elif "restart the system" in data_btn:       #Not Executed
        speak.speak("Restarting the system...")
        os.system("shutdown /r /t 5")
        return "Restarting the system..." 

#13
    elif "close command prompt" in data_btn:       #Execution Successful
        text = "Closing Command Prompt"
        speak.speak(text)
        os.system("taskkill /f /im cmd.exe")
        return text
#14
    elif "close notepad" in data_btn:       #Execution Successful
        text = "Closing NotePad"
        speak.speak(text)
        os.system("taskkill /f /im notepad.exe")
        return text
#15
    elif "close microsoft word" in data_btn:       #Execution Successful
        text1 = "Closing Microsoft Word"
        speak.speak(text1)
        os.system("wmic process where \"name='winword.exe'\" delete")
        return text1
#16
    elif "close microsoft excel" in data_btn:       #Execution Successful
        text1 = "Closing microsoft excel"
        speak.speak(text1)
        os.system("taskkill /f /im excel.exe")
        return text1
#17
    elif "close microsoft powerpoint" in data_btn:       #Execution Successful
        text1 = "Closing Powerpoint"
        speak.speak(text1)
        os.system("taskkill /f /im powerpnt.exe")
        return text1
#18
    elif 'open chrome' in data_btn:       #Execution Successful
        text = "Opening Google Chrome"
        speak.speak(text)
        npath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        os.startfile(npath)
        return text
#19
    elif 'maximize this window' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        text = 'Maximizing this window'
        speak.speak(text)
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('x')
        return text
#20
    elif 'google search' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        data_btn = data_btn.replace("google search", "")
        pyautogui.hotkey('alt', 'd')
        pyautogui.write(f"{data_btn}", 0.1)
        pyautogui.press('enter')
#21
    elif 'open new window' in data_btn:       #Execution Successful 
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.hotkey('ctrl', 'n')

#22
    elif 'open incognito window' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.hotkey('ctrl', 'shift', 'n')
#23
    elif 'minimise this window' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.hotkey('alt', 'space')
        time.sleep(1)
        pyautogui.press('n')
#24
    elif 'open history' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.hotkey('ctrl', 'h')
#25
    elif 'open downloads' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.hotkey('ctrl', 'j')
#26
    elif 'previous tab' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.hotkey('ctrl', 'shift', 'tab')
#27
    elif 'next tab' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.hotkey('ctrl', 'tab')
#28
    elif 'close tab' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.hotkey('ctrl', 'w')
#29
    elif 'close window' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.hotkey('ctrl', 'shift', 'w')
#30
    elif 'clear browsing history' in data_btn:       #Execution Successful 
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.hotkey('ctrl', 'shift', 'delete')
#31
    elif 'close chrome' in data_btn:       #Execution Successful
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        os.system("taskkill /f /im chrome.exe")

    elif 'search on youtube' in data_btn:
        search_query = data_btn.replace('search on youtube', '').strip()
        webbrowser.open(f'https://www.youtube.com/results?search_query={search_query}')
        speak.speak(f"Here are the search results for {search_query} on YouTube.")
        return f"Here are the search results for {search_query} on YouTube."
    
    elif "pause" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.press('space bar')
        time.sleep(2) 

    elif "resume" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.press('space bar')
        time.sleep(2)

    elif "full screen" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.press('f')
        time.sleep(2)

    elif "film screen" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.press('t')
        time.sleep(2)

    elif "skip" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.press('l')
        time.sleep(2)

    elif "back" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.press('j')
        time.sleep(2)

    elif "mute" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.press('m')
        time.sleep(2)

    elif "umute" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.press('m')  
        time.sleep(2)

    elif "previous video" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        press_and_release('SHIFT + p')
        time.sleep(2)

    elif "next" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        press_and_release('SHIFT + n')  
        time.sleep(2)

    elif "volume up" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.press('up')
        pyautogui.press('space bar')
        time.sleep(2)

    elif "volume down" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        move_cursor()
        pyautogui.click() 
        sleep(1)
        pyautogui.press('space bar')
        pyautogui.press('down')
        time.sleep(2)
        
        
#32
    # elif "take screenshot" in data_btn:
    #         speak.speak("Sir, Please tell me the name for the screenshot file")
    #         name = takeCommand()
    #         print(name)
    #         speak.speak("Taking Screenshot...!")
    #         time.sleep(2)
    #         img = pyautogui.screenshot()
    #         img.save(f"{name}.png")
    #         speak.speak("ScreenShot Saved...!")
    #         return "ScreenShot Saved...!"
    elif "take screenshot" in data_btn:
        speak.speak("Please select the folder where you want to save the screenshot.")
        folder_path = filedialog.askdirectory()
        if folder_path:
            speak.speak("Please tell me what should be the name for the screenshot file")
            name = takeCommand()
            print(name)
            speak.speak("Taking Screenshot...!")
            time.sleep(2)
            img = pyautogui.screenshot()
            file_path = os.path.join(folder_path, f"{name}.png")
            img.save(file_path)
            speak.speak("Screenshot Saved...Opening Screenshot!")
            
            # Open the saved screenshot using PIL
            saved_image = Image.open(file_path)
            saved_image.show()  # Display the saved screenshot
            
            return "Screenshot Saved...opening Screenshot!"
        else:
            return "No folder selected. Screenshot not saved."
#33
    elif 'wikipedia' in data_btn:       #Execution Successful       --incomplete Work
        speak.speak('Searching Wikipedia...')
        results = wikipedia.summary(data_btn, sentences=2)
        speak.speak("According to Wikipedia")
        speak.speak(results)
        return results
#34
    elif "turn the volume up" in data_btn:       #Execution Successful
        pyautogui.press("volumeup")
#35
    elif "turn the volume down" in data_btn:       #Execution Successful
        pyautogui.press("volumedown")
#36
    elif "mute" in data_btn:       #Execution Successful
        pyautogui.press("volumemute")
#37
    elif "stop" in data_btn:
        exit()
#38
    elif "draw square spiral" in data_btn:
        pyautogui.press('win')
        sleep(1)
        keyboard.write('paint')
        sleep(2)
        keyboard.press('enter')
        sleep(0.5)
        move_cursor()
        sleep(0.5)
        square_spiral()
#39
    elif "draw square" in data_btn:
        pyautogui.press('win')
        sleep(1)
        keyboard.write('paint')
        sleep(2)
        keyboard.press('enter')
        sleep(0.5)
        move_cursor()
        sleep(0.5)
        drawSquare()
#40
    elif "draw house" in data_btn:
        pyautogui.press('win')
        sleep(1)
        keyboard.write('paint')
        sleep(2)
        keyboard.press('enter')
        sleep(0.5)
        move_cursor()
        sleep(0.5)
        drawHouse()

    #45
    elif "open a file" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        sleep(1)
        pyautogui.hotkey('ctrl', 'o')
#12
    elif "open" in data_btn:
        Nameoftheapp = data_btn.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)  
        return True
    
 #43
    elif "save this file" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        sleep(1)
        pyautogui.hotkey('ctrl', 's')
#44
    elif "new file" or "new tab" in data_btn:
        pyautogui.hotkey('alt', 'esc')
        sleep(1)
        pyautogui.hotkey('ctrl', 'n')
           
#41
           
    elif "update to do list" in data_btn:
        response = add_data_to_sheet_speech()
        return response
    
    elif "show me my progress" in data_btn:
        show_tableau_dashboard()
        return "Opening Tableau dashboard..."

    elif 'tell me' in data_btn:
        try:
            res = chat1(data_btn)
            speak.speak(res);
            return res;
        except Exception as e:
            speak.speak( "i'm unable to understand!")
            return "i'm unable to understand!" 
    
    
    elif "make a note" in data_btn:
        pyautogui.press('win')
        sleep(1)
        keyboard.write('notepad')
        sleep(2)
        keyboard.press('enter')
        sleep(0.5)
        speak.speak('What to note?')
        text = takeCommand()
        pyautogui.write(text) 
        return "noted"
    
    elif "news" in data_btn:
        ans = NewsRead.latestnews() 
        speak.speak(ans)
        return "Here are the latest news articles."

    # Your existing code...

    else:
        speak.speak("I'm unable to understand!")
        return "I'm unable to understand!"
    



    
        
        

