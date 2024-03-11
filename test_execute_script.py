from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
import math

try :

    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")
    getting_answer_to_capcha=int(browser.find_element(By.CSS_SELECTOR,"div :nth-child(2)").text)
    print(getting_answer_to_capcha)
    counting_answer_to_capha=math.log(abs(12*math.sin(getting_answer_to_capcha)))
    getting_input_fild_to_answer=browser.find_element(By.CSS_SELECTOR, 'input,[class="form-control"]')
    getting_input_fild_to_answer.send_keys(counting_answer_to_capha)
    clicking_chechbox=browser.find_element(By.ID, 'robotCheckbox').click()
    getting_radiobutton=browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);",getting_radiobutton)
    getting_radiobutton.click()
    button_submit=browser.find_element(By.CSS_SELECTOR, 'button,[class="btn btn-primary"]').click()


finally :
    time.sleep(10)

    browser.quit()