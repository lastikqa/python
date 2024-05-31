from bs4 import BeautifulSoup
import requests
import pprint
word_soups = []

url = 'https://english4life.ru/top-200-frazovyx-glagolov-anglijskogo-yazyka.html'
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

words = soup.findAll('tr')

for data in words:
    word_soup = []
    for j in data:
        if j.text != "\n":
            text = j.text
            if "*" in text:
                text = text.replace("*", "")
            word_soup.append(text)
    word_soups.append(word_soup)
pprint.pprint(word_soups)
counter = 0

with open("phrasal_verbs.py", "w", encoding='utf-8') as file:
    file.write("phrasall_verbs = {")
    for i in range( len(word_soups)-1):
        counter += 1
        if counter == len(word_soups):
            file.write(f'"{word_soups[i][0]}": {word_soups[i][1:-1]}')
            file.write("}")
        else:
            file.write(f'"{word_soups[i][0]}": {word_soups[i][1:-1]},\n')
    file.write(f'"{word_soups[counter][0]}": {word_soups[counter][1:-1]}')
    file.write("}")