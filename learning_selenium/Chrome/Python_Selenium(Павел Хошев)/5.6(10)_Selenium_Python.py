import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


with webdriver.Chrome() as browser:

    browser.get('https://parsinger.ru/selenium/5.5/5/1.html')

    style_div_list = browser.find_elements(By.XPATH, "//div[contains(@style, 'background')]")

    for i in range(1, len(style_div_list)+1):
        xpath = f"//div[contains(@style, 'background')][{i}]"
        hex_color = browser.find_element(By.XPATH, f"{xpath}/span").text

        select = Select(browser.find_element(By.XPATH, f"{xpath}/select"))
        select.select_by_visible_text(hex_color)

        browser.find_element(By.XPATH, f"{xpath}/div/button[@data-hex='{hex_color}']").click()

        browser.find_element(By.XPATH, f"{xpath}/input[1]").click()

        browser.find_element(By.XPATH, f"{xpath}/input[2]").send_keys(hex_color)

        browser.find_element(By.XPATH, f"{xpath}").click()

    for i in range(1, len(style_div_list)+1):
        xpath = f"//div[contains(@style, 'background')][{i}]"
        browser.find_element(By.XPATH, f"{xpath}/button").click()

    browser.find_element(By.XPATH, "//body/button").click()

    alert = browser.switch_to.alert.text
    print(alert)
