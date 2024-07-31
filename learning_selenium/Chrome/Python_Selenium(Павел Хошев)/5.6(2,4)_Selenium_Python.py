import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/1/1.html')
    input_fields = browser.find_elements(By.CSS_SELECTOR, "input.text-field")
    for i in input_fields:
        i.clear()
    button = browser.find_element(By.CSS_SELECTOR, "button#checkButton").click()

    alert = browser.switch_to.alert.text
    print(alert)

with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/5.5/2/1.html')
    input_fields = browser.find_elements(By.CSS_SELECTOR, "input.text-field")
    for i in input_fields:
        if i.is_enabled():
            i.clear()
    button = browser.find_element(By.CSS_SELECTOR, "button#checkButton").click()

    alert = browser.switch_to.alert.text
    print(alert)