from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

browser = webdriver.Chrome()

try :
    browser.get(" http://suninjuly.github.io/explicit_wait2.html")

    getting_price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element(
        (By.ID, "price"), "100"))
    if getting_price == True :
        getting_button_buy = browser.find_element(By.CSS_SELECTOR, 'button[onclick="checkPrice();"]').click()
    getting_capcha_question = int(browser.find_element(By.ID, "input_value").text)
    getting_capcha_inputfields = browser.find_element(By.ID, 'answer')
    getting_submut_button = browser.find_element(By.ID, 'solve')
    counting_answer_to_capha = math.log(abs(12 * math.sin(getting_capcha_question)))
    getting_capcha_inputfields.send_keys(counting_answer_to_capha)
    getting_submut_button.click()
    alert = browser.switch_to.alert

    assert getting_capcha_question.is_integer(), ('getting_capcha_question must be int')
    assert browser.switch_to.alert==True ," alert is not found"
finally :

    time.sleep(10)
    browser.quit()
