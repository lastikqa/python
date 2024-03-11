from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    getting_requred_ibputfields=browser.find_elements(By.CSS_SELECTOR, 'div label input,[required=""]')
    counter_of_requred_ibputfields=0
    for requred_ibputfield in  getting_requred_ibputfields :
        time.sleep(2)
        requred_ibputfield.send_keys('Hello World')
        counter_of_requred_ibputfields += 1

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
    assert counter_of_requred_ibputfields == 3 ,(f"requred_ibputfields were changed")
finally:

    time.sleep(10)
    browser.quit()