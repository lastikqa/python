from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get('https://testautomationpractice.blogspot.com/')
getting_wikepedia_icon = driver.find_element(By.CLASS_NAME, 'wikipedia-icon')
getting_wikepedia_inputfield = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
getting_wikepedia_search_button = driver.find_element(By.CLASS_NAME, 'wikipedia-search-button')
getting_wikepedia_h1 = driver.find_element(By.TAG_NAME, 'h1').text
print(getting_wikepedia_h1)
time.sleep(5)
driver.quit()
