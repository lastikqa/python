import time
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


options = Options()
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0 ")
#options.add_argument("--headless")
options.page_load_strategy = 'normal'
options.add_argument("--disable-blink-features=AutomationControlled")
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", f"{os.getcwd()}\\downloads")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(options=options)

action = ActionChains(driver)

driver.get("https://hyperskill.org/login")
driver.switch_to.new_window("tab")

driver.get(" https://www.avito.ru/")
driver.switch_to.new_window("tab")

driver.get("https://www.ozon.ru/")
driver.refresh()

windows = driver.window_handles

print(windows)
driver.switch_to.window(driver.window_handles[0]) # hyperskill
print(driver.title)
button_pricing=driver.find_element(By.XPATH, '(//div//li)[3]').click()
time.sleep(2)

driver.switch_to.window(windows[1]) #avito
print(driver.title)
button_career=driver.find_element(By.XPATH, '(//li/a)[2]').click()
time.sleep(2)

driver.switch_to.window(windows[2]) #ozon
print(driver.title)
button_ozon_carta=driver.find_element(By.XPATH, '(//li/a)[1]').click()


print(len(windows))

time.sleep(5)

driver.quit()