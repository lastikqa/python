from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try :

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    getting_first_name_inputfield=browser.find_element(By.CSS_SELECTOR,'input,[name="firstname"]')
    getting_first_name_inputfield.send_keys("Python")
    getting_last_name_inputfield=browser.find_element(By.CSS_SELECTOR,'div input:nth-child(4)')
    getting_last_name_inputfield.send_keys('is')
    getting_email_inputfield = browser.find_element(By.CSS_SELECTOR, 'div [name="email"]')
    getting_email_inputfield.send_keys("cool")
    getting_dowload_inputfield = browser.find_element(By.CSS_SELECTOR, 'div input:nth-child(5)')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_file.txt')
    getting_dowload_inputfield.send_keys(file_path)
    getting_button_submit=browser.find_element(By.CSS_SELECTOR, 'button,[type="submit"]').click()



finally :
    time.sleep(10)

    browser.quit()