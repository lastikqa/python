
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_localisation(browser,language) :
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."
    browser.get(link)
    wait = WebDriverWait(browser, 30, poll_frequency=1)
    add_to_basket = wait.until(EC.element_to_be_clickable(browser.find_element(By.XPATH, "(//button)[3]"))).text
    print(language)

    if language == "ru" :
        assert add_to_basket == "Добавить в корзину", f"Your localisation must be ru, now your is {language} "
    elif language == 'en-gb' :
        assert add_to_basket == "Add to basket", f"Your localisation must be en-gb, now your is {language} "
    else :
        print(f"  {language} is not suppotred, u might have isues.")
    time.sleep(5)