import pyttsx3 #pip install pyttsx3
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib
from time import sleep

import support
import memory


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
volume = engine.getProperty("volume")
speak_velocity = engine.getProperty("rate")
assistant_name = "Yummi"

engine.setProperty("voice", voices[0].id) # 0 para inglês e 1 para português
engine.setProperty("rate", 170)

def speak(text="there is nothing to say"):
    """
    Write anything that you want your assistant to say.

    :param text: The text you want to pass to your assistant
    """
    engine.say(text)
    engine.runAndWait()


def wish_me():
    """
    This function control the way your assistant will wish you
    """
    hour = int(datetime.datetime.now().hour)

    if hour > 6 and hour < 12:
        speak("Good Morning Master")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Master")
    elif hour >= 18 and hour <= 23:
        speak("Good Evening Master")
    else:
        speak("It's midnight, nice to see you master")

wish_me()