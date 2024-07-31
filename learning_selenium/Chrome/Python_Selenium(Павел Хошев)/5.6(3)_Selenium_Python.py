import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint

with webdriver.Chrome() as browser:
    total = 0
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    selected_values = [int(x['value']) for x in cookies if int(x['name'].rsplit("_")[-1]) % 2 == 0]
    for i in selected_values:
        total +=i
    print(total)