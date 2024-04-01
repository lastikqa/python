import time
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from dowloading_files import list_names_of_download_files

"""dowloading_files.py must be runned firt"""

options = Options()
# options.add_argument("--user-agent=Ваш кастомный или заранее выбранный юзер-агент")
options.add_argument("--headless")
options.page_load_strategy = 'normal'
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", f"{os.getcwd()}\\downloads")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(options=options)


driver.get('http://the-internet.herokuapp.com/upload')

for file in list_names_of_download_files :
    choosing_file = driver.find_element(By.XPATH, "//input[@name='file']")
    time.sleep(1)
    choosing_file.send_keys(f"{os.getcwd()}\\downloads\\{file}")
    time.sleep(1)
    upload_button = driver.find_element(By.XPATH, "//input[@id='file-submit']").click()
    time.sleep(1)
    uploaded_files = driver.find_element(By.XPATH, "//div[@id='uploaded-files']").text
    time.sleep(1)
    assert file == uploaded_files, "wrong data"
    driver.back()
    time.sleep(1)

time.sleep(10)
driver.quit()
