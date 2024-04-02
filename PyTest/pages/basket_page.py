from PyTest.conftest import language
from PyTest.pages.base_page import BasePage
from PyTest.pages.locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_login_url()
        self.should_be_basket_header()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "basket" in url, "this is not the basket page"

    def should_be_basket_header(self):
        basket_header_text = self.browser.find_element(*BasketPageLocators.basket_header).text
        if language == "ru":
            assert basket_header_text == "Корзина", (f"Your header is {basket_header_text},"
                                                     f"The header should be 'Корзина'")
        elif language == "en-gb":
            assert basket_header_text == "Basket", f"Your header is {basket_header_text}, The header should be 'Basket'"
        else:
            print(f" the {language} localisation is not supported")

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.basket_message), "The message should say about empty basket"

    def should_be_no_goods_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.basket_goods), "Goods should not be in basket"

    def should_be_goods_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.basket_goods), ("The added goods are not in basket, "
                                                                           "there should be added goods")
