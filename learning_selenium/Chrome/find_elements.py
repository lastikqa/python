import time
from selenium import webdriver
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/1/1.html')
    input_form = browser.find_elements(By.TAG_NAME, "input")
    for i in input_form:
        print(i)
        i.send_keys("Hello_Selenium")
    time.sleep(1)
    browser.find_element(By.ID,"btn").click()
    time.sleep(20)