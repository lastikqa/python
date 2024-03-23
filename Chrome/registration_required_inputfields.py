from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)
first_name= browser.find_element(By.CSS_SELECTOR, "div:nth-child(1) input[required='']")
first_name.send_keys('Hello')
time.sleep(2)
last_name = browser.find_element(By.CSS_SELECTOR,"div:nth-child(2) input[required='']")
last_name.send_keys('World')
time.sleep(2)
email = browser.find_element(By.CSS_SELECTOR,"div:nth-child(3) input[required='']")
email.send_keys('python@selenium.org')
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(2)

welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text
assert welcome_text=="Congratulations! You have successfully registered!"



time.sleep(10)
browser.quit()