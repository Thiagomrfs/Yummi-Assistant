import json
import os
import datetime
from cipherdef_by_Biel import cipher


current = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
try:
    os.chdir("memory")
except:
    os.system("mkdir memory")
    os.chdir("memory")


def add_website_to_memory(new_website):
    with open("websites.json", "r+") as memory:
        data = json.load(memory)
    
    data.append(new_website)

    with open("websites.json", "w+", encoding="utf8") as memory:
        json.dump(data, memory, indent=4, separators=(",", ":"), ensure_ascii=False)

def get_websites_in_memory():
    with open("websites.json", "r+") as memory:
        data = json.load(memory)
    return data

def remove_website_from_memory(removed_one):
    with open("websites.json", "r+") as memory:
        data = json.load(memory)
    
    data.pop(data.index(removed_one))

    with open("websites.json", "w+", encoding="utf8") as memory:
        json.dump(data, memory, indent=4, separators=(",", ":"), ensure_ascii=False)

def add_password_to_memory(query, indentifier):
    with open("passwords.json", "r+") as memory:
        data = json.load(memory)

    encripted = cipher(query["password"], indentifier, 1)
    finished = {query["site"]: encripted}
    data.append(finished)

    with open("passwords.json", "w+", encoding="utf8") as memory:
        json.dump(data, memory, indent=4, separators=(",", ":"), ensure_ascii=False)

def get_passwords_from_memory():
    with open("passwords.json", "r+", encoding="utf8") as memory:
        data = json.load(memory)
    return data

def remove_password_from_memory(removed_one):
    with open("passwords.json", "r+") as memory:
        data = json.load(memory)
    
    data.pop(data.index(removed_one))

    with open("passwords.json", "w+", encoding="utf8") as memory:
        json.dump(data, memory, indent=4, separators=(",", ":"), ensure_ascii=False)

def add_birthday_reminder(query):
    with open("birthdays.json", "r+") as memory:
        data = json.load(memory)
    
    data.append(query)

    with open("birthdays.json", "w+", encoding="utf8") as memory:
        json.dump(data, memory, indent=4, separators=(",", ":"), ensure_ascii=False)

def get_birthdays():
    with open("birthdays.json", "r+") as memory:
        data = json.load(memory)
    return data

def actualize_birthday_year():
    data = get_birthdays()
    for entry in data:
        for name, birthday in entry.items():
            today = datetime.date.today()
            birthdate = datetime.date(birthday[0], birthday[1], birthday[2])
            if today > birthdate:
                birthday[0] += 1
    with open("birthdays.json", "w", encoding="utf8") as memory:
        json.dump(data, memory, indent=4, separators=(",", ":"), ensure_ascii=False)


if "websites.json" not in os.listdir():
    with open("websites.json", "w+") as a:
        a.write("""[
    {
        "Youtube":"https://youtube.com"
    },
    {
        "Github":"https://github.com"
    },
    {
        "Lofi":"https://www.youtube.com/watch?v=5qap5aO4i9A"
    },
    {
        "Discord":"https://discord.com/"
    }
]""")

if "passwords.json" not in os.listdir():
    with open("passwords.json", "w+") as a:
        a.write("[]")

if "birthdays.json" not in os.listdir():
    with open("birthdays.json", "w+") as a:
        a.write("[]")

actualize_birthday_year()
