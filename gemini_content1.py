from config import key
import requests

def chat1(chat):
    messages = []
    system_message = "You are an AI Virtual Assistant created by Vidisha, Yakuta, Akshada, your name is AVY."
    message = { "role" : "user", "parts" : [{"text": 'give me the answer of ' + system_message + " " + chat +  'in maximum of 40 words' }]}
    messages.append(message)
    data = {'contents' : messages}
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key="+key
    response = requests.post(url, json=data)
    t1 = response.json()
    t2 = t1.get("candidates")[0].get("content").get("parts")[0].get("text")
    t3 = t2.replace('*', '')
    print(t3)

if __name__ == "__main__":
    chat = "cwho is ms dhoni"
    chat1(chat)