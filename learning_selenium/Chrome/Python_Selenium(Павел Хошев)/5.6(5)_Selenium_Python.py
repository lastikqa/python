import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint

with webdriver.Chrome() as browser:
    link_dict = {}
    browser.get('https://parsinger.ru/methods/5/index.html')
    raw_links = browser.find_elements(By.CSS_SELECTOR, "a[href]")

    for i in raw_links:
        link_dict[i.get_attribute('href')] = None

    for link in link_dict:
        browser.get(link)
        cookies = browser.get_cookies()
        link_dict[link] = int(cookies[0]["expiry"])

    link_dict = sorted(link_dict.items(), key=lambda x: x[1])
    browser.get(link_dict[-1][0])  # link_dict(link, cookie)
    number = browser.find_element(By.CSS_SELECTOR, "p#result").text
    print(number)
