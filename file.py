import pickle
import time
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium.common.exceptions import NoAlertPresentException

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

driver.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019')

adding_to_bucket = driver.find_element(By.XPATH, "(//button)[3]").click()

WebDriverWait(driver, 3).until(EC.alert_is_present())
alert = driver.switch_to.alert
x = alert.text.split(" ")[2]
answer = str(math.log(abs((12 * math.sin(float(x))))))
alert.send_keys(answer)
alert.accept()
try:
    WebDriverWait(driver, 120).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert_text = alert.text
    print(f"Your code: {alert_text}")
    alert.accept()
except NoAlertPresentException:
    print("No second alert presented")

driver.refresh()
book_name=(By.TAG_NAME,"h1")
add_to_basket=(By.XPATH,"(//button)[3]")
message_of_success=(By.XPATH,"(//div[@class='alertinner '])[1]")
message_of_current_action=(By.XPATH,"(//div[@class='alertinner'])[2]")
price_of_basket=(By.CSS_SELECTOR,"div [class='alert alert-safe alert-noicon alert-info  fade in']")
price_of_book=(By.CSS_SELECTOR,"div p[class='price_color']")


book_name=driver.find_element(*book_name).text
message_of_adding =driver.find_element(*message_of_success).text
assert book_name in message_of_adding , "The added book is not correct"
price_of_basket=driver.find_element(*price_of_basket).text
price_of_book=driver.find_element(*price_of_book).text
assert price_of_book in price_of_basket , "The price is wrong"