import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


with webdriver.Chrome() as browser:
    span_list = []
    browser.get('https://parsinger.ru/selenium/5.7/5/index.html')
    elements = browser.find_elements(By.CSS_SELECTOR, "div button")
    for element in elements:
        seconds = element.get_attribute("value")
        ActionChains(browser).click_and_hold(element).pause(float(seconds)).release(element).perform()
    alert = browser.switch_to.alert.text
    print(alert)




