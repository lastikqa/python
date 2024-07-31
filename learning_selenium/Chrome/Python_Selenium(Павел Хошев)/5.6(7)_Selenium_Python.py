import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint

with webdriver.Chrome() as browser:
    total = 0
    browser.get('https://parsinger.ru/scroll/4/index.html')
    buttons = browser.find_elements(By.CSS_SELECTOR, "button.btn")
    for button in buttons:
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()
        number = browser.find_element(By.CSS_SELECTOR, "p#result").text
        total += int(number)

    print(total)