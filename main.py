import pyttsx3 #pip install pyttsx3
import speech_recognition as sr # pip install speechRegonition
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import smtplib
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
volume = engine.getProperty("volume")
speak_velocity = engine.getProperty("rate")
assistant_name = "Yummi"

engine.setProperty("voice", voices[1].id)
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
    
    # speak(f"How can I help you?")


def take_command():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        command.adjust_for_ambient_noise(source)
        audio = command.listen(source)

    try:
        print("Recognizing...")
        query = command.recognize_google(audio, language="en-us")
        print(f"User said: {query}\n")
    except Exception as error:
        speak("Sorry, I didn't understand")
        query = ""
    finally:
        return query

        
# print(f"Initializing...")
# speak(f"initializing {assistant_name}...")
# sleep(0.5)
wish_me()
query = take_command()

if "wikipedia" in query.lower():
    speak("Searching Wikipedia...")
    try:
        query = query.replace("wikipedia", "")
    except:
        query = query.replace("Wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)