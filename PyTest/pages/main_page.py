from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .login_page import LoginPage
class MainPage(BasePage):

    def go_to_login_page(self) :
        wait = WebDriverWait(self.browser, 30, poll_frequency=1)
        self.browser.find_element(By.XPATH, "(//li/a)[1]").click()
        #alert = self.browser.switch_to.alert
        #alert.accept()
        return LoginPage(browser=self.browser, url=self.browser.current_url)
    def should_be_login_link(self) :
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"