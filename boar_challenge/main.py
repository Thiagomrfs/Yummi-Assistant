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

engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 160)

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

support.msg("Good evening master, how can I help you?")
wish_me()
resp, option = support.menu(["Open website",
                            "Search meaning",
                            "Create shortcut",
                            "Recieve command"
                            "exit"])

os.system("cls")
speak(f"You choosed: {option}")


if resp == 1:
    support.msg("open website")
    websites = memory.get_websites_in_memory()
    query = []

    for website in websites:
        for key in website:
            query.append(key)
    query.append("add new website")
    query.append("remove website")
    selected, option = support.menu(query)

    for website in websites:
        for site, url in website.items():
            if site == option:
                speak("opening website")
                webbrowser.open(url, new=2)
    if option == "add new website":
        details = {}
        name = input("What's the name of the website? ")
        print("\033[32mTip: http:/mywebsite.com\033[m")
        url = input("what's the url of the website? ")
        details[name] = url
        memory.add_website_to_memory(details)
    elif option == "remove website":
        os.system("cls")
        support.msg("which website do you want to remove?")
        index, removed_one = support.menu(query[:-2])
        for website in websites:
            for site, url in website.items():
                if site == removed_one:
                    memory.remove_website_from_memory(website)
elif resp == 2:
    support.msg("Search meaning")
    term = input("Wich term do you want to search about? ")
    response = wikipedia.summary(term, sentences=2)
    print()
    print(response)
    speak(response)
elif resp == 3:
    pass
elif resp == 4:
    pass
elif resp == 5:
    pass
elif resp == 6:
    pass