from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try :
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    getting_rolling_button=browser.find_element(By.CSS_SELECTOR, 'button,[type="submit"]').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    getting_capha_question = int(browser.find_element(By.XPATH,'//div[1]/label/span[2]').text)
    counting_answer_to_capha = math.log(abs(12 * math.sin(getting_capha_question)))
    getting_capha_inputfield = browser.find_element(By.ID, 'answer')
    getting_capha_inputfield.send_keys(counting_answer_to_capha)
    getting_submut_button= browser.find_element(By.CSS_SELECTOR, 'button,[type="submit"]').click()

finally :
    time.sleep(10)

    browser.quit()
