from selenium.webdriver.common.by import By


class BasketPageLocators:
    basket_header = (By.TAG_NAME, "h1")
    basket_message = (By.CSS_SELECTOR, "div[id='content_inner'] p")
    basket_goods = (By.XPATH, "//div/h3")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    basket_button = (By.CSS_SELECTOR, "a[class='btn btn-default']")
    search_button = (By.CSS_SELECTOR, "input[type='submit']")
    basket_price = (By.XPATH, "//div[@class='basket-mini pull-right hidden-xs']")
    oscar_button = (By.XPATH, "(//header//div/a)[1]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    language_select = (By.CSS_SELECTOR, "select[name='language']")
    submit_language = (By.CSS_SELECTOR,"button[type='submit']")


class MainPageLocators:
    welcome_text = (By.XPATH, "(//div[@class='sub-header'])[1]/h2")
    recommended_reading = (By.XPATH, "(//div[@class='sub-header'])[2]/h2")
    other_good_books = (By.XPATH, "(//div[@class='sub-header'])[3]/h3")


class LoginPageLocators:
    login_form = (By.CSS_SELECTOR, "form[id='login_form']")
    register_form = (By.CSS_SELECTOR, "form[id='register_form']")
    register_email_address = (By.CSS_SELECTOR, "input[id='id_registration-email']")
    register_password = (By.CSS_SELECTOR, "input[id='id_registration-password1']")
    register_confirm_password = (By.CSS_SELECTOR, "input[id='id_registration-password2']")
    register_button = (By.CSS_SELECTOR, "button[name='registration_submit']")
    registration_success = (By.XPATH, "(//div[@class='alertinner wicon'])[1]")


class ProductPageLocators:
    book_name = (By.TAG_NAME, "h1")
    add_to_basket = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    message_of_success = (By.XPATH, "(//div[@class='alertinner ']/strong)[1]")
    message_of_current_action = (By.XPATH, "(//div[@class='alertinner '])[2]")
    price_of_basket = (By.XPATH, "(//div[@class='alertinner ']/p/strong)")
    price_of_book = (By.CSS_SELECTOR, "div p[class='price_color']")
