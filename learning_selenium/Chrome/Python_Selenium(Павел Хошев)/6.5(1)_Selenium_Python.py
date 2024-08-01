import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    total = 0
    browser.get('https://parsinger.ru/scroll/2/index.html')
    checkboxes = browser.find_elements(By.CSS_SELECTOR, "div.item")
    for i in range(1, len(checkboxes)+1):
        browser.find_element(By.XPATH, f"//div/div[{i}]/input").click()
        number = browser.find_element(By.XPATH,f"//div/div[{i}]/div/p/span").text
        total += int(number) if number.isdigit() else 0
    print(total)
