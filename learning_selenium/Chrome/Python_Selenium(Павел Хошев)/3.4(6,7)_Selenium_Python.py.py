
from selenium import webdriver
from selenium.webdriver.common.by import By


# all numbers
total = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    elements = browser.find_elements(By.CSS_SELECTOR, "div p")
    for element in elements:
        total += int(element.text)
    print(total)


# each second element in div p
total_second = 0
with webdriver.Chrome() as browser:
    browser.get('https://parsinger.ru/selenium/3/3.html')
    elements = browser.find_elements(By.CSS_SELECTOR, "div")
    for i in range(len(elements)-1):
        element = browser.find_element(By.XPATH, f"//div[1]/div[{1+i}]/p[2]").text  # looks so great
        total_second += int(element)

    print(total)