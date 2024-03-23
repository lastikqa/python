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

driver.get('http://selenium1py.pythonanywhere.com/ru/catalogue/category/books_2/')

adding_to_bucket = driver.find_element(By.XPATH, "(//section//li//button)[1]").click()
bucket = driver.find_element(By.XPATH, "(//header/div/div/div)[2]").text

assert "Всего в корзине: 9,99 £" in bucket, f"the bucket must be 9,99 £, your bucket is {bucket}"


pickle.dump(driver.get_cookies(), open(os.getcwd() + r"/downloads/cookies.pkl", "wb"))
driver.delete_all_cookies()
driver.refresh()

bucket = driver.find_element(By.XPATH, "(//strong)[1]").text
assert bucket == "Всего в корзине:", "your bucket must be empty"

cookies = pickle.load(open(os.getcwd() + "/downloads/cookies.pkl", "rb"))
for cookie in cookies :
    driver.add_cookie(cookie)

driver.refresh()

bucket = driver.find_element(By.XPATH, "(//header/div/div/div)[2]").text
assert "Всего в корзине: 9,99 £" in bucket, f"the bucket must be 9,99 £, your bucket is {bucket}"


driver.get("https://n5m.ru/usagent.html")

user_agent = driver.find_element(By.TAG_NAME, "h1").text

print(user_agent)

time.sleep(20)
driver.quit()
