from PyTest.conftest import language
from PyTest.pages.base_page import BasePage
from PyTest.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_login_url()
        self.should_be_basket_header()

    def should_not_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.basket_message), ("Message of empty basket is presented,"
                                                                                 "but should not be")

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "basket" in url, "this is not the basket page"

    def should_be_basket_header(self):
        basket_header_text = self.browser.find_element(*BasketPageLocators.basket_header).text
        if language == "ru":
            assert basket_header_text == "Корзина", f"Your header is {basket_header_text},The header should be 'Корзина'"
        elif language == "en-gb":
            assert basket_header_text == "Basket", f"Your header is {basket_header_text}, The header should be 'Basket'"

    def should_be_empty_basket(self):
        basket_message = self.browser.find_element(*BasketPageLocators.basket_message).text
        if language == "ru":
            assert basket_message == "Ваша корзина пуста.", (f"Your Basket message is {basket_message}, "
                                                             f"The header should be 'Ваша корзина пуста.'")
        elif language == "en-gb":
            assert basket_message == "Your basket is empty.", (f"Your Basket message is {basket_message}, "
                                                               f"The header should be 'Your basket is empty.'")
