from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from PyTest.pages.locators import BasePageLocators
from PyTest.conftest import language


class BasePage:
    def go_to_main_page(self):
        self.browser.find_element(*BasePageLocators.oscar_button).click()

    def go_to_basket(self):
        self.browser.find_element(*BasePageLocators.basket_button).click()

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        WebDriverWait(self.browser, timeout, poll_frequency=1)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

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

    def open(self):
        self.browser.get(self.url)

    def basket_price_status(self):
        basket_price = self.browser.find_element(*BasePageLocators.basket_price).text
        return basket_price

    def should_be_empty_basket_price(self):
        basket_price = self.basket_price_status()
        if language == "ru":
            assert basket_price == "0,00£", f"Your Basket price is {basket_price}, The price should be '0,00£'"
        elif language == "en-gb":
            assert basket_price == "£0.00", f"Your Basket price is {basket_price}, The price should be '£0.00'"
