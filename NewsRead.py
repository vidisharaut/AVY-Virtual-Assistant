import requests
import json
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query
    except Exception as e:
        print("Say that again please...")
        return "None"



def latestnews():
    api_dict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=4c85af7df92440aea27bc337f664ecac",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=4c85af7df92440aea27bc337f664ecac",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=4c85af7df92440aea27bc337f664ecac",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=4c85af7df92440aea27bc337f664ecac",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=4c85af7df92440aea27bc337f664ecac",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=4c85af7df92440aea27bc337f664ecac"
    }

    content = None
    url = None
    news_articles = ""  # Initialize an empty string to store news articles
    speak("Which field news do you want, [business], [health], [technology], [sports], [entertainment], [science]?")
    field = take_command().lower()
    for key, value in api_dict.items():
        if key.lower() in field:
            url = value
            print("URL was found:", url)
            break
    else:
        print("URL not found for the given category:", field)
        return "No news articles found."

    try:
        news = requests.get(url).json()
        speak("Here are the top 5 news articles.")

        arts = news["articles"][:5]  # Limit to top 5 articles
        for articles in arts:
            article = articles["title"]
            news_articles += article + ". "  # Concatenate news articles
            print(article)
            speak(article)
            news_url = articles["url"]
            print(f"For more info visit: {news_url}")

        speak("That's all for the top 5 news articles")
        return news_articles  # Return the concatenated news articles
    except Exception as e:
        print("An error occurred:", e)
        return "An error occurred while fetching news articles."


if __name__ == "__main__":
    latestnews()

