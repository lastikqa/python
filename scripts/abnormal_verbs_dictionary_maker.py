from bs4 import BeautifulSoup
import requests
import pprint
word_soups = []

url = 'https://usefulenglish.ru/writing/irregular-verbs'
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

with open("abnormal_verbs.py", "w", encoding='utf-8') as file:
    file.write("abnormal_verbs = {")
    for i in range(2, len(word_soups)-1):
        counter += 1
        if counter == len(word_soups)-3:
            file.write(f'"{word_soups[i][0]}": {word_soups[i]}')
            file.write("}")
        else:
            file.write(f'"{word_soups[i][0]}": {word_soups[i]},\n')
