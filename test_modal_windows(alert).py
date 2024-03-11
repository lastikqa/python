import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try :
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')
    getting_alert_button = browser.find_element(By.CSS_SELECTOR, 'button,[class="btn btn-primary"]').click()
    alert = browser.switch_to.alert
    alert.accept()
    getting_capha_question = int(browser.find_element(By.XPATH, '//div[1]/label/span[2]').text)
    counting_answer_to_capha = math.log(abs(12 * math.sin(getting_capha_question)))
    getting_capha_inputfield = browser.find_element(By.ID, 'answer')
    getting_capha_inputfield.send_keys(counting_answer_to_capha)
    getting_submut_button = browser.find_element(By.CSS_SELECTOR, 'button,[type="submit"]').click()



finally :
    time.sleep(10)

    browser.quit()
