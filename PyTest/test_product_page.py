from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser) :
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.clicing_adding_button()
    page.should_be_message_about_adding()
    time.sleep(10)
