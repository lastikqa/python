import time

import pytest
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.urls import ProductPageUrl
from .pages.urls import LoginPageUrl
@pytest.mark.add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.login_page = LoginPage(browser, LoginPageUrl.login_url)
        self.login_page.open()
        self.login_page.register_new_user()
        self.login_page.registration_successfully_message()

    def test_user_cant_see_success_message(self, browser) :
        self.product_page = ProductPage(browser,ProductPageUrl.product_url)
        self.product_page.open()
        self.product_page.should_not_be_success_message()


    def test_user_can_add_product_to_basket(self,browser) :
        self.product_page = ProductPage(browser, ProductPageUrl.product_url)
        self.product_page.open()
        self.product_page.clicing_adding_button()
        self.product_page.should_be_message_about_adding()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, ProductPageUrl.product_url)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    page = BasePage(browser, ProductPageUrl.product_url)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPageUrl.product_url)
    page.open()
    page.clicing_adding_button()
    page.should_be_message_about_adding()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageUrl.product_url)
    page.open()
    page.clicing_adding_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPageUrl.product_url)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPageUrl.product_url)
    page.open()
    page.clicing_adding_button()
    page.should_not_message_disappeared_after_adding_product_to_basket()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = ProductPage(browser, ProductPageUrl.product_url)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_no_goods_in_basket()
    basket.should_be_empty_basket_message()


def test_guest_can_go_to_main_page(browser):
    page = ProductPage(browser, ProductPageUrl.product_url)
    page.open()
    page.go_to_main_page()
    main_page = MainPage(browser, browser.current_url)
    main_page.should_be_main_page()
