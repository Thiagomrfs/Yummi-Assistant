from googletrans import Translator
from googletrans import LANGUAGES
from time import sleep
import datetime
import os

import memory


def clear_screen():
    sleep(1)
    try:
        os.system("cls")
    except:
        os.system("clear")

def msg(text, cor=""):
    print(f"\033[{cor}m"+"="*(len(text)+4))
    print(text.center(len(text)+4))
    print("="*(len(text)+4)+"\033[m")

def menu(options:list):
    count = 1
    for option in options:
        print(f"\033[34m{count}\033[m - \033[33m{option}\033[m")
        count +=1
    print()
    resp = verify_int(input("Please choose an option: "), range(1, count+1))
    return resp, list(options)[resp - 1]

def verify_int(value, accepted):
    try:
        if int(value) in accepted:
            return int(value)
        else:
            raise TypeError
    except:
        while True:
            try:
                value = int(input("\033[31mPlease insert a valid value: \033[m"))
                if value in accepted:
                    break
                    return int(value)
            except:
                continue

def translate():
    msg("Select source language")
    src, source = menu(LANGUAGES.values())
    clear_screen()
    msg("Select destination language")
    dest, destination = menu(LANGUAGES.values())
    clear_screen()
    text = input("Insert the text that will be translated: ")
    translator = Translator()
    response = translator.translate(text, src=source, dest=destination)
    return response.text

def check_near_birthdays():
    data = memory.get_birthdays()
    near = []
    for entry in data:
        for name, date in entry.items():
            birthday = datetime.date(date[0], date[1], date[2])
            today = datetime.date.today()
            delta = birthday - today
            if delta.days < 8:
                near.append(name)
    return near
