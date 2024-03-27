from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage) :
    def should_be_login_page(self) :
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self) :
        url = self.browser.current_url
        assert "login" in url, "this is not the login page"

    def should_be_login_form(self) :
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self) :
        assert self.is_element_present(*LoginPageLocators.register_form), "Register formk is not presented"
