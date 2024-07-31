import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


with webdriver.Chrome() as browser:
    total = 0
    browser.get('https://parsinger.ru/selenium/7/7.html')
    elements = browser.find_elements(By.CSS_SELECTOR, "select#opt")
    for item in elements:
        for element in item.text.split('\n'):
            element = element.strip()
            if element.isdigit():
                total += int(element)
    browser.find_element(By.ID, "input_result").send_keys(str(total))
    browser.find_element(By.CSS_SELECTOR, "input#sendbutton").click()
    #time.sleep(10)

with webdriver.Chrome() as browser:
    should_find = str(((12434107696 * 3) * 2) +1)
    browser.get('https://parsinger.ru/selenium/6/6.html')
    select = Select(browser.find_element(By.CSS_SELECTOR,"select#selectId"))
    select.select_by_visible_text(should_find)
    browser.find_element(By.CSS_SELECTOR, "input#sendbutton").click()
    time.sleep(10)
