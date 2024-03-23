from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get('https://www.selenium.dev/')
print(driver.title)
assert driver.title == "Selenium", "wrong page"
driver.get('https://www.chromium.org/chromium-projects/')
print(driver.title)
assert driver.title == "Home", 'wrong page'
driver.back()
assert driver.title == "Selenium", "wrong page"
driver.refresh()
page_url = driver.current_url
assert page_url == ('https://www.selenium.dev/'), "wronge page"
driver.forward()

time.sleep(5)
driver.quit()
