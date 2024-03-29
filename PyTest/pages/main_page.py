from .base_page import BasePage

from .locators import MainPageLocators
from .urls import MainPageUrl


class MainPage(BasePage):
    def should_be_main_page(self):
        self.should_be_main_page_url()
        self.should_be_welcome_text()
        self.should_be_recommended_reading()
        self.should_be_other_good_books()

    def should_be_main_page_url(self):
        main_url = self.browser.current_url

        assert "login" not in main_url, (f"The current url is {main_url},"
                                         f"The url should be {MainPageUrl.main_page_url}")

        assert "catalogue" not in main_url, (f'The current url is {main_url},'
                                             f'The url should be {MainPageUrl.main_page_url}')

        assert "basket" not in main_url, (f'The current url is {main_url},'
                                          f'The url should be {MainPageUrl.main_page_url}')

    def should_be_welcome_text(self):
        assert self.is_element_present(MainPageLocators.welcome_text), ("the recommended reading sub-header should be "
                                                                        "presented")

    def should_be_recommended_reading(self):
        assert self.is_element_present(
            MainPageLocators.recomended_reading), "the welcome sub-header should be presented"

    def should_be_other_good_books(self):
        assert self.is_element_present(
            MainPageLocators.other_good_books), "the other good books sub-header should be presented"
