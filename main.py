import speech_recognition as sr
from modules.speech import speak
from modules.commands import log, processCommand

if __name__ == "__main__":

    speak("Initializing Jarvis")

    r = sr.Recognizer()

    while True:

        print("Recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")

                audio = r.listen(
                    source,
                    timeout=3,
                    phrase_time_limit=5
                )

            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes, how can I assist you?")

                with sr.Microphone() as source:

                    log("Jarvis active...")

                    audio = r.listen(source)

                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:

            print("Sorry, I did not understand that.")
            print(e)


