import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage




def test_guest_can_go_to_login_page(browser) :
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser) :
    link = "http://selenium1py.pythonanywhere.com"
    page=MainPage(browser,link)
    page.open()
    page.go_to_basket()
    time.sleep(10)

