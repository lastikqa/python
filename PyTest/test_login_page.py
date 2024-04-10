from .pages.login_page import LoginPage
from .pages.urls import LoginPageUrl
from .pages.main_page import MainPage


def test_guest_can_go_to_main_page(browser):
    login_page = LoginPage(browser, LoginPageUrl.login_url)
    login_page.open()
    login_page.should_be_login_page()
    login_page.go_to_main_page()
    main_page = MainPage(browser, browser.current_url)
    main_page.should_be_main_page()


def test_guest_can_be_authorizated_with_login_and_password(browser):
    login_page = LoginPage(browser, LoginPageUrl.login_url)
    login_page.open()
    login_page.should_be_login_page()
    login_page.putting_login_email()
    login_page.putting_login_password()
    login_page.clicking_login_button()
    login_page.should_be_message_about_autorisation()


def test_guest_cannot_be_authorizated_without_password(browser):
    login_page = LoginPage(browser, LoginPageUrl.login_url)
    login_page.open()
    login_page.should_be_login_page()
    login_page.putting_login_email()
    login_page.clicking_login_button()
    login_page.should_not_be_message_about_autorisation()

