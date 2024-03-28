from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
class MainPageLocators() :
    pass


class LoginPageLocators() :
    login_form = (By.CSS_SELECTOR, "form[id='login_form']")
    register_form = (By.CSS_SELECTOR, "form[id='register_form']")


class ProductPageLocators() :
    book_name = (By.TAG_NAME, "h1")
    add_to_basket = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    message_of_success = (By.XPATH, "(//div[@class='alertinner ']/strong)[1]")
    message_of_current_action = (By.XPATH, "(//div[@class='alertinner '])[2]")
    price_of_basket = (By.XPATH, "(//div[@class='alertinner ']/p/strong)")
    price_of_book = (By.CSS_SELECTOR, "div p[class='price_color']")
