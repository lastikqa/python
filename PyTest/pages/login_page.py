from .locators import LoginPageLocators
from .base_page import BasePage
import faker
from .test_data import loginPageTestData


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        url = self.browser.current_url
        assert "login" in url, "this is not the login page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.register_form), "Register form is not presented"

    def putting_login_email(self):
        login_email = self.browser.find_element(*LoginPageLocators.login_email)
        login_email.send_keys(loginPageTestData.email)

    def putting_login_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.login_password)
        login_password.send_keys(loginPageTestData.password)

    def clicking_login_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.login_button)
        login_button.click()

    def should_be_message_about_autorisation(self):
        assert self.is_element_present(*LoginPageLocators.login_success)\
            , "there should be message about autorisation"

    def should_not_be_message_about_autorisation(self):
        assert self.is_not_element_present(*LoginPageLocators.login_success)\
            , "there should not be message about autorisation"

    def register_new_user(self):
        f = faker.Faker()
        email = f.email()
        password = f.password()
        self.browser.find_element(*LoginPageLocators.register_email_address).send_keys(email)
        self.browser.find_element(*LoginPageLocators.register_password).send_keys(password)
        self.browser.find_element(*LoginPageLocators.register_confirm_password).send_keys(password)
        self.browser.find_element(*LoginPageLocators.register_button).click()
        assert self.is_element_present(*LoginPageLocators.registration_success), "The registration was failed"
