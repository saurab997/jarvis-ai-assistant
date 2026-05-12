import webbrowser
from modules.speech import speak
from modules.ai import aiResponse
from modules.news import get_news
from modules import musiclibrary
from datetime import datetime

def log(msg):
    print(f"[Jarvis{datetime.now().strftime('%H:%M:%S')}] {msg}")

def processCommand(c):

    if "open google" in c.lower():

        log("Opening Google")
        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    elif "open facebook" in c.lower():

        log("Opening Facebook")
        speak("Opening Facebook")

        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in c.lower():

        log("Opening YouTube")
        speak("Opening Youtube")

        webbrowser.open("https://www.youtube.com")

    elif "open instagram" in c.lower():

        log("Opening Instagram")
        speak("Opening Instagram")

        webbrowser.open("https://www.instagram.com")

    elif c.lower().startswith("play"):

        log("Playing music")
        song = c.lower().split(" ")[1]

        link = musiclibrary.music[song]

        webbrowser.open(link)

    elif "news" in c.lower():

        log("Fetching news")
        articles = get_news()

        for article in articles:

            log("Reading news title")
            speak(article["title"])

    else:

        log("Processing AI response")
        output = aiResponse(c)

        log(output)
        speak(output)