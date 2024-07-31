import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    total = 0
    browser.get('https://parsinger.ru/methods/3/index.html')
    cookies = browser.get_cookies()
    for i in cookies:
        if "secret_cookie"in i["name"]:
            total += int(i["value"])
    print(total)