import time
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument("--user-agent=Ваш кастомный или заранее выбранный юзер-агент")
options.add_argument("--headless")
options.page_load_strategy = 'normal'
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", f"{os.getcwd()}\\downloads")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(options=options)

list_names_of_download_files = []

driver.get('http://the-internet.herokuapp.com/download')
try :

    elements = driver.find_elements(By.XPATH, "//a")
    for i in range(len(elements) - 1) :
        list_names_of_download_files.append(elements[i].text)
        elements = driver.find_elements(By.XPATH, "//div/div/div/a")
        elements[i].click()
    time.sleep(2)
    assert len(list_names_of_download_files) == len(elements), "something does not appear in downloads"
    list_names_of_download_files.pop()
    list_names_of_download_files.pop(0)

    print(list_names_of_download_files)

finally :

    time.sleep(10)
    driver.quit()
