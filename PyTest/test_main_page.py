from .pages.basket_page import BasketPage
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_page()


def test_guest_see_product_in_basket_opened_from_main_page(browser):   # positive
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_empty_basket_price()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_empty_basket()


def test_guest_cannt_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.should_be_empty_basket_price()
    page.go_to_basket()
    basket = BasketPage(browser, browser.current_url)
    basket.should_not_be_empty_basket()
