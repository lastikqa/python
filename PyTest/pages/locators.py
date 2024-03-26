from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "a[id='login_link']")


class LoginPageLocators():
    login_form=(By.CSS_SELECTOR,"form[id='login_form']")
    register_form=(By.CSS_SELECTOR,"form[id='register_form']")
