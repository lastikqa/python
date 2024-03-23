from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


def answer_capcha(capcha_first_number: int, capcha_second_number: int, capcha_operator: str) -> int :
    # the function counting answer to capcha
    if capcha_operator == "+" :
        return capcha_first_number + capcha_second_number
    elif capcha_operator == "-" :
        return capcha_first_number - capcha_second_number


try :
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    capcha_first_number = browser.find_element(By.ID, "num1")
    capcha_first_number = int(capcha_first_number.text)
    capcha_second_number = browser.find_element(By.ID, "num2")
    capcha_second_number = int(capcha_second_number.text)
    capcha_operator = browser.find_element(By.CSS_SELECTOR, "div :nth-child(3)").text
    answer_into_dropbox = answer_capcha(capcha_first_number, capcha_second_number, capcha_operator)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(f"{answer_into_dropbox}")
    clicking_submit_button = browser.find_element(By.CSS_SELECTOR, 'div button,[type="submit"]').click()


finally :
    time.sleep(10)

    browser.quit()
