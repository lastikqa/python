import time
from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    gray_number_list = []
    browser.get('https://parsinger.ru/selenium/5.5/4/1.html')
    gray_numbers = browser.find_elements(By.XPATH, "//div/textarea[1]")
    for number in gray_numbers:
        gray_number_list.append(number.text)
        number.clear()

    blue_numbers = browser.find_elements(By.XPATH, "//div/textarea[2]")

    counter = 0
    for number in blue_numbers:
        number.send_keys(gray_number_list[counter])
        counter += 1
    buttons = browser.find_elements(By.XPATH,"//div/button")

    for button in buttons:
        button.click()

    button = browser.find_element(By.CSS_SELECTOR, "button#checkAll").click()

    time.sleep(15)