import time
import os
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver.implicitly_wait(10) making driver to wait for n- seconds (using after initialization of driver)

options = Options()
# options.add_argument("--headless")
options.page_load_strategy = 'normal'
options.set_preference("browser.download.folderList", 2)
options.set_preference("browser.download.manager.showWhenStarting", False)
options.set_preference("browser.download.dir", f"{os.getcwd()}\\downloads")
options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

driver = webdriver.Firefox(options=options)  # initialization of driver

wait = WebDriverWait(driver, 30, poll_frequency=1)
# (what waits) (how many seconds to wait) (how many times to request at second)


driver.get('https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver')
try :
    button_open_alert_5_seconds = driver.find_element(By.ID, 'alert')
    button_open_alert_5_seconds.click()
    alert = wait.until(EC.alert_is_present(), f'alert is not found')
    alert.accept()

    button_change_text = driver.find_element(By.CSS_SELECTOR, "button[id='populate-text']").click()
    text_of_the_button = (By.CSS_SELECTOR, "h2[id='h2']")
    wait.until(EC.text_to_be_present_in_element(text_of_the_button, 'Selenium Webdriver'), "text not found")

    button_after_10_seconds = driver.find_element(By.ID, 'display-other-button').click()
    button_enable = (By.CSS_SELECTOR, 'button[id="hidden"]')
    wait.until(EC.visibility_of_element_located(button_enable), "button is not found")

    enable_button_after_10_seconds = driver.find_element(By.ID, "enable-button").click()
    button = (By.ID, "disable")
    wait.until(EC.element_to_be_clickable(button), f"button is not aviable to click")

    check_checkbox_after_10_seconds = driver.find_element(By.ID, "checkbox").click()
    checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
    wait.until(EC.element_located_to_be_selected(checkbox), f"checkbox is not checked")

finally :
    time.sleep(10)
    driver.quit()
