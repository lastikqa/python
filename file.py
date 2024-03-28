import pickle
import time
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.add_argument("--width=1000")
options.add_argument("--height=800")
options.add_argument("--disable-blink-features=AutomationControlled")  # to disable "im a robot"
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0 ")
#options.add_argument("--headless")
options.page_load_strategy = 'normal'
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", f"{os.getcwd()}\\downloads")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(options=options)
wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
click=driver.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']").click()
book_name =driver.find_element(By.TAG_NAME, "h1").text

message_of_success = driver.find_element(By.XPATH, "(//div[@class='alertinner ']/p/strong)").text


print(book_name)
print(message_of_success)

time.sleep(30)
driver.quit()



