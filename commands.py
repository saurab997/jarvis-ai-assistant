import webbrowser
from modules.speech import speak
from modules.ai import aiResponse
from modules.news import get_news
from modules import musiclibrary

def processCommand(c):

    if "open google" in c.lower():

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    elif "open facebook" in c.lower():

        speak("Opening Facebook")

        webbrowser.open("https://www.facebook.com")

    elif "open youtube" in c.lower():

        speak("Opening Youtube")

        webbrowser.open("https://www.youtube.com")

    elif "open instagram" in c.lower():

        speak("Opening Instagram")

        webbrowser.open("https://www.instagram.com")

    elif c.lower().startswith("play"):

        song = c.lower().split(" ")[1]

        link = musiclibrary.music[song]

        webbrowser.open(link)

    elif "news" in c.lower():

        articles = get_news()

        for article in articles:

            speak(article["title"])

    else:

        output = aiResponse(c)

        speak(output)