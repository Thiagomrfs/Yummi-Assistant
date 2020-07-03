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
user_path_name = "Nilcy Marinho"

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

        
print(f"Initializing {assistant_name}...")
sleep(0.5)
wish_me()
query = take_command()

if "wikipedia" in query.lower():
    speak("Searching Wikipedia...")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    print(results)
    speak(results)
elif "open code" in query.lower():
    speak("opening code")
    code_path=f"C:\\Users\\{user_path_name}\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

elif "open youtube" in query.lower():
    speak("opening youtube")
    webbrowser.open("https:/youtube.com", new=2)
elif "open google" in query.lower():
    speak("opening google")
    webbrowser.open("https:/google.com", new=2)
elif "open github" in query.lower():
    speak("opening github")
    webbrowser.open("https:/github.com", new=2)

elif "chill your mind" in query.lower():
    speak("opening chill your mind radio")
    webbrowser.open("https://www.youtube.com/watch?v=eQdA8dvsgQs", new=2)
elif "play lo-fi" in query.lower():
    speak("opening lo-fi radio")
    webbrowser.open("https://www.youtube.com/watch?v=5qap5aO4i9A", new=2)

elif "time now" in query.lower():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    print(f"It is {hour} hours and {minute} minutes")
    speak(f"It is {hour} hours and {minute} minutes")
    

sleep(2)
os.system("cls")
