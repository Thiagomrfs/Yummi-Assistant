import pyttsx3 #pip install pyttsx3
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import getpass
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
    user = getpass.getuser()
    if hour > 6 and hour < 12:
        support.msg(f"Good morning {user}, how can I help you?")
        speak(f"Good Morning {user}")
    elif hour >= 12 and hour < 18:
        support.msg(f"Good afternoon {user}, how can I help you?")
        speak(f"Good Afternoon {user}")
    elif hour >= 18 and hour <= 23:
        support.msg(f"Good evening {user}, how can I help you?")
        speak(f"Good Evening {user}")
    else:
        speak(f"It's midnight, nice to see you {user}")


wish_me()
resp, option = support.menu(["Open website",
                            "Search meaning",
                            "Translate",
                            "Get passwords",
                            "Add pasword",
                            "Exit"])

os.system("cls")
speak(f"You choosed: {option}")


if option == "Open website":
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
        support.support.clear_screen()
        support.msg("which website do you want to remove?")
        index, removed_one = support.menu(query[:-2])
        for website in websites:
            for site, url in website.items():
                if site == removed_one:
                    memory.remove_website_from_memory(website)
    support.clear_screen()
elif option == "Search meaning":
    support.msg("Search meaning")
    term = input("Wich term do you want to search about? ")
    speak("searching")
    response = wikipedia.summary(term, sentences=2)
    print()
    print(response)
    speak(response)
    support.clear_screen()
elif option == "Translate":
    output = support.translate()
    print(f"The translated text is: {output}")
elif option == "Get passwords":
    pass
elif option == "Add password":
    pass
elif option == "Exit":
    exit()