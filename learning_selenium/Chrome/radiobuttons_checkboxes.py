import pickle
import time
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
driver = webdriver.Chrome(options=options)
# wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get('https://demoqa.com/selectable')

grid_status = driver.find_element(By.XPATH, '//nav/a[@id="demo-tab-grid"]').get_attribute("aria-selected")
grid = driver.find_element(By.XPATH, '//nav/a[@id="demo-tab-grid"]')
assert grid_status == "false"
grid.click()

grid_status = driver.find_element(By.XPATH, '//nav/a[@id="demo-tab-grid"]').get_attribute("aria-selected")

assert grid_status == "true"

one_status = driver.find_element(By.XPATH, "(//div/li)[1]").get_attribute("class")

assert "active" not in one_status, "element one must be disabled"
one = driver.find_element(By.XPATH, "(//div/li)[1]")
one.click()

one_status = driver.find_element(By.XPATH, "(//div/li)[1]").get_attribute("class")
assert "active" in one_status, "element one must be enabled"

one = driver.find_element(By.XPATH, "(//div/li)[1]")
one.click()

one_status = driver.find_element(By.XPATH, "(//div/li)[1]").get_attribute("class")
assert "active" not in one_status, "one bust be disabled"

driver.quit()