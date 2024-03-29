from PyTest.conftest import language
from PyTest.pages.base_page import BasePage


class BasketPage(BasePage) :
    def should_be_basket_page(self) :
        self.should_be_login_url()
        self.should_be_basket_header()

    def should_be_login_url(self) :
        url = self.browser.current_url
        assert "basket" in url, "this is not the basket page"

    def should_be_basket_header(self) :
        basket_header_text = self.browser.find_lement().text
        if language == "ru" :
            assert basket_header_text == "Корзина", f"Your header is {basket_header_text}, The header should be 'Корзина'"
        elif language == "en-gb" :
            assert basket_header_text == "Basket", f"Your header is {basket_header_text}, The header should be 'Basket'"
