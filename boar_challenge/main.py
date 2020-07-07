import pyttsx3 #pip install pyttsx3
import datetime
import wikipedia # pip install wikipedia
import webbrowser
import os
import getpass
from time import sleep

import support
import memory
from cipherdef_by_Biel import cipher


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

def show_near_birthdays():
    near = support.check_near_birthdays()
    print(f"\033[36mNear birthdays: {', '.join(near)}\033[m")


wish_me()
while True:
    show_near_birthdays()
    resp, option = support.menu(["Open website",
                                "Search meaning",
                                "Translate",
                                "Get passwords",
                                "Add password",
                                "Add birthday reminder",
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
        sleep(10)
        support.clear_screen()
    elif option == "Get passwords":
        support.msg("Password manager")
        print("\033[31mBe sure to write it correctly!!!\033[m")
        main_password = input("Insert your main password: ")
        data = memory.get_passwords_from_memory()
        keys = []
        for entry in data:
            for key, value in entry.items():
                decripted = cipher(value, main_password, 2)
                print(f"\033[34m{key}\033[m - \033[33m{decripted}\033[m")
        print("\033[mIf the passwords here has no sense, probably your main password is wrong!\033[m")
    elif option == "Add password":
        support.msg("Adding new password")
        query = {}
        print("\033[31mBe sure to remember this, you can't change it later!!!\033[m")
        print("\033[31mAnd you need it to get the passwords, so write it out!!!\033[m")
        main_password = input("Insert your main password: ")
        query["site"] = input("For wich site do you want to store te password? ")
        query["password"] = input("Insert the password: ")
        memory.add_password_to_memory(query, main_password)
    elif option == "Add birthday reminder":
        support.msg("Adding birthday reminder")
        query = {}
        today = datetime.date.today()
        who = input("it's whose birthday? [name] ")
        day = support.verify_int(input("what day will it happen? "), range(1, 31))
        month = support.verify_int(input("what month will it happen? "), range(1, 13))
        year = 0
        if today.day > day:
            if today.month > month:
                year = today.year + 1
            else:
                year = today.year
        else:
            year = today.year
        query[who] = [year, month, day]
        memory.add_birthday_reminder(query)
    elif option == "Exit":
        exit()
    
    support.clear_screen()