from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.urls import MainPageUrl


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MainPageUrl.main_page_url)
    page.open()
    page.go_to_login_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MainPageUrl.main_page_url)
    page.open()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_no_goods_in_basket()
    basket.should_be_empty_basket_message()
