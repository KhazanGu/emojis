import requests
from bs4 import BeautifulSoup

url = "https://unicode.org/emoji/charts/emoji-list.html"


def getHtml(url):
    html = requests.get(url)
    return html

def soup(content):
    emojis = ""
    category_emojis = ""

    soup = BeautifulSoup(content)
    table = soup.find("table")
    all_tr = table.find_all("tr")
    for tr in all_tr:
        th = tr.find("th", class_="bighead")
        if th:
            a = th.find("a")
            if a:
                print(category_emojis)
                category_emojis = ""
                category = a.text
                print("Category: " + category)
        all_td = tr.find_all("td", class_="andr")
        for td in all_td:
            all_img = td.find_all("img", class_="imga")
            for img in all_img:
                alt = img["alt"]
                category_emojis += alt
                emojis += alt
    print(category_emojis)
    print("All emojis:\n" + emojis)



html = getHtml(url)
soup(html.content)
