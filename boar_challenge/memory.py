import json
import os

current = os.getcwd()
os.chdir(os.path.dirname(os.path.abspath(__file__)))
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

if "websites.json" not in os.listdir():
    a = open("websites.json", "w+")
    a.write("[]")
    a.close()