from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get('https://hyperskill.org/tracks')

# "button_hyperskill":(By.XPATH,'(//div/ul/li)[1]/a') none clicing by my autotest


header_interactive_elements = {
    "pricing_button" : (By.XPATH, '(//div//li)[3]'),
    "button_sing_up" : (By.XPATH, "//div//button[1]"),
    "button_start_for_free" : (By.XPATH, "//div//button[2]"),
    "for_business_button" : (By.XPATH, "(//div//li//a)[4]")
}

expected_pages = ["pricing", "login", "register", "for-organizations"]
counter_of_pages = -1

try :
    for key, value in header_interactive_elements.items() :
        time.sleep(5)
        if key == 'for_business_button' :
            clicking_button = driver.find_element(value[0], value[1]).click()
            time.sleep(5)
            counter_of_pages += 1
            new_window = driver.window_handles[1]
            driver.switch_to.window(new_window)
            c_url = driver.current_url
            print(c_url, expected_pages[counter_of_pages], sep="   ")
            assert expected_pages[counter_of_pages] in c_url, "wrong_page"
            time.sleep(5)
            driver.close()
        else :
            clicking_button = driver.find_element(value[0], value[1]).click()
            counter_of_pages += 1
            c_url = driver.current_url
            assert expected_pages[counter_of_pages] in c_url, "wrong_page"
            print(c_url, expected_pages[counter_of_pages], sep="   ")
            time.sleep(10)
            driver.back()


finally :
    time.sleep(10)
    driver.quit()
