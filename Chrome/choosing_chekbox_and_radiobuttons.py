from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x) :
    return str(math.log(abs(12 * math.sin(int(x)))))


try :
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    element = browser.find_element(By.ID, "treasure")
    x = element.get_attribute("valuex")
    print(x)
    y = calc(x)
    element = browser.find_element(By.ID, "answer")
    element.send_keys(y)
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    button = browser.find_element(By.CSS_SELECTOR, '[type=submit]')
    button.click()

finally :

    time.sleep(10)

    browser.quit()
