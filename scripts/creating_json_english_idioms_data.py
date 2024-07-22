from bs4 import BeautifulSoup
import requests
import json
word_soups = []

url = 'https://www.fluentu.com/blog/english/idioms/'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

words = soup.findAll('h3')
description = soup.findAll('p')

first_index=0
last_index = 0
for i in description:
    if "If someone says they’re going to hit the hay" in i.text:
        first_index = description.index(i)
    if "If a plan or effort bears fruit" in i.text:
        last_index = description.index(i)

values = []
for i in range(first_index, last_index, 2):
    value = description[i].text
    values.append(value)


json_idioms_data = {}
keys = []

try:
    for i in words:
        keys.append(i.text.split("         ")[1].split("\n")[0].strip())
finally:
    for i in range(len(keys)):
        if keys[i] not in json_idioms_data:
            json_idioms_data[keys[i]] = values[i]

    with open("english_idioms_data.json", "w", encoding="utf-8") as file:
        json.dump(json_idioms_data, file, indent=2)

