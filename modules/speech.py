import pyttsx3
from gtts import gTTS
import pygame
import os

engine = pyttsx3.init()

def speak_old(text):
   engine.say(text)
   engine.runAndWait()

def speak(text):
   tts = gTTS(text)
   tts.save("temp.mp3")

   pygame.mixer.init() #initialize pygame mixer

   pygame.mixer.music.load("temp.mp3") #load mp3

   pygame.mixer.music.play() #play the mp3

   while pygame.mixer.music.get_busy(): #wait for the music to finish playing
      pygame.time.Clock().tick(10)

   pygame.mixer.music.unload() #unload the mp3
   os.remove("temp.mp3") #delete mp3 file