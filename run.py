import requests
from bs4 import BeautifulSoup

# https://emojipedia.org/

emojipedia = "https://emojipedia.org/"

# Categories
people = emojipedia + "people"
nature = emojipedia + "nature"
food_drink = emojipedia + "food-drink"
activity = emojipedia + "activity"
travel_places = emojipedia + "travel-places"
objects = emojipedia + "objects"
symbols = emojipedia + "symbols"
flags = emojipedia + "flags"

urls = [people, nature, food_drink, activity, travel_places, objects, symbols, flags]

def getHtml(url):
    html = requests.get(url)
    return html.content

def soup(content):
    emojis = ""
    soup = BeautifulSoup(content)
    ul = soup.find("ul", class_="emoji-list css_test1")
    # print(ul)
    li_all = ul.find_all("li")
    for li in li_all:
        span = li.find("span", class_="emoji")
        if span:
            # print(span.text)
            emojis += span.text
    return emojis



# all emojis

allEmojis = ""

for url in urls:
    content = getHtml(url)
    emojis = soup(content)
    allEmojis += emojis
    category = url.split("/")[-1]
    print(category + ":\n" + emojis)

print("all emojis:\n" + allEmojis)


