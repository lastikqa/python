
from .base_page import BasePage
from .locators import ProductPageLocators
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException



class ProductPage(BasePage) :
    def should_be_product_page(self) :
        self.should_not_be_success_message()
        self.clicing_adding_button()
        self.solve_quiz_and_get_code()
        self.should_be_message_about_adding()
        self.should_not_message_disappeared_after_adding_product_to_basket()

    def clicing_adding_button(self) :
        wait = WebDriverWait(self.browser, 30, poll_frequency=1)
        wait.until(EC.element_to_be_clickable(self.browser.find_element(*ProductPageLocators.add_to_basket))).click()

    def solve_quiz_and_get_code(self) :
        WebDriverWait(self.browser, 2, poll_frequency=1).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try :
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException :
            print("No second alert presented")

    def should_be_message_about_adding(self) :
        assert self.is_element_present(*ProductPageLocators.message_of_success), "the basket is empty"

        book_name = self.browser.find_element(*ProductPageLocators.book_name).text
        message_of_success = self.browser.find_element(*ProductPageLocators.message_of_success).text

        assert book_name == message_of_success, f"The added book is {message_of_success}, it should be {book_name}"

        price_of_basket = self.browser.find_element(*ProductPageLocators.price_of_basket).text
        price_of_book = self.browser.find_element(*ProductPageLocators.price_of_book).text

        assert price_of_book in price_of_basket, f"The basket price is {price_of_basket}, the price shoul be {price_of_book} "

    def should_not_be_success_message(self) :
        assert self.is_not_element_present(*ProductPageLocators.message_of_success), \
            "Message of success is presented, but should not be"


    def should_not_message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(ProductPageLocators.message_of_success), \
            "Message of success did, but should not be"
