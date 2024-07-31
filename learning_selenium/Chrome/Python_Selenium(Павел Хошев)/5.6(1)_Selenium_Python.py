import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/methods/1/index.html')
    number = browser.find_element(By.CSS_SELECTOR, "p#result").text
    while number.isdigit() == False:
        browser.refresh()
        number = browser.find_element(By.CSS_SELECTOR, "p#result").text
    print(number)