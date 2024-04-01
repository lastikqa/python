from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from PyTest.pages.locators import BasePageLocators
from PyTest.pages.test_data import Language
from selenium.webdriver.support.select import Select
from PyTest.pages.test_data import SearchItem
import math


class BasePage:
    def go_to_main_page(self):
        self.browser.find_element(*BasePageLocators.oscar_button).click()

    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.basket_button).click()

    def go_to_login_page(self):
        self.browser.find_element(*BasePageLocators.LOGIN_LINK).click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException :
            print("No second alert presented")


    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def change_language(self):
        select = Select(self.browser.find_element(*BasePageLocators.language_select))
        select.select_by_visible_text(Language.chosen_language[0])
        self.browser.find_element(*BasePageLocators.submit_language).click()

    def should_be_changed_language(self):
        url_language = self.browser.current_url
        assert Language.chosen_language[1] in url_language, f'the language should be {Language.chosen_language[0]}'

    def searching_products(self):
        self.browser.find_element(*BasePageLocators.search_input_field).send_keys(SearchItem.search_item)
        self.browser.find_element(*BasePageLocators.search_click).click()

    def should_be_searched_product(self):
        assert self.is_element_present(*BasePageLocators.found_product), "Product was not found"

    def open(self):
        self.browser.get(self.url)

    def basket_price_status(self):
        basket_price = self.browser.find_element(*BasePageLocators.basket_price).text
        return basket_price

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"
