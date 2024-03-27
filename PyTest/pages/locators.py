from selenium.webdriver.common.by import By


class MainPageLocators() :
    LOGIN_LINK = (By.CSS_SELECTOR, "a[id='login_link']")


class LoginPageLocators() :
    login_form = (By.CSS_SELECTOR, "form[id='login_form']")
    register_form = (By.CSS_SELECTOR, "form[id='register_form']")


class ProductPageLocators() :
    book_name = (By.TAG_NAME, "h1")
    add_to_basket = (By.XPATH, "(//button)[3]")
    message_of_success = (By.XPATH, "(//div[@class='alertinner '])[1]")
    message_of_current_action = (By.XPATH, "(//div[@class='alertinner'])[2]")
    price_of_basket = (By.CSS_SELECTOR, "div [class='alert alert-safe alert-noicon alert-info  fade in']")
    price_of_book = (By.CSS_SELECTOR, "div p[class='price_color']")
