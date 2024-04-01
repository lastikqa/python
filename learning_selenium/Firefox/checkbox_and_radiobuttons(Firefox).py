import pickle
import time
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

options = Options()
options.add_argument("--width=1000")
options.add_argument("--height=800")
options.add_argument("--disable-blink-features=AutomationControlled")  # to disable "im a robot"
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0 ")
# options.add_argument("--headless")
options.page_load_strategy = 'normal'
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", f"{os.getcwd()}\\downloads")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

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
