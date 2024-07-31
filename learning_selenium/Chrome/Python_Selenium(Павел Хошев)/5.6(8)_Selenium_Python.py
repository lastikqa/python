import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    total = 0
    browser.get('https://parsinger.ru/selenium/5.5/3/1.html')
    checkboxes = browser.find_elements(By.CSS_SELECTOR, "input.checkbox")
    print(len(checkboxes))
    for i in range(1, len(checkboxes)+1):
        checkbox = browser.find_element(By.XPATH, f"//div/div[{i}]/input")
        if checkbox.is_selected():
            number = browser.find_element(By.XPATH, f"//div/div[{i}]/textarea").text
            total += int(number)
    print(total)
