from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()

driver.get("https://demoqa.com/text-box")
try :
    full_name=driver.find_element(By.ID,"userName").clear()
    email=driver.find_element(By.CSS_SELECTOR,"input.userEmail").clear()
    current_address=driver.find_element(By.ID,"currentAddress").clear()
    pepmament_address=driver.find_element(By.ID,"pepmamentAddress").clear()

    assert full_name.get_attribute() == "", "full_name is not empty"
    assert email.get_attribute() == "", "email is not empty"
    assert current_address.get_attribute() == "", "current_address is not empty"
    assert pepmament_address.get_attribute() == "", "pepmament_address is not empty"



finally :

    time.sleep(5)
    driver.quit()