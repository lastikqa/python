from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()

driver.get("http://the-internet.herokuapp.com/status_codes")

try :
    status_code_200=driver.find_element(By.XPATH,'(//ul/li)[1]/a').click()
    time.sleep(5)
    url=driver.current_url
    assert '200' in url, 'wrong page'
    driver.back()
    time.sleep(5)
    assert 'status_codes' in url , "wrong page"
    status_code_301=driver.find_element(By.XPATH,'(//ul/li)[2]/a').click()
    time.sleep(5)
    url = driver.current_url
    assert '301' in url, 'wrong page'
    driver.back()
    time.sleep(5)
    status_code_404 = driver.find_element(By.XPATH, '(//ul/li)[3]/a').click()
    time.sleep(5)
    url = driver.current_url
    assert "404" in url , "wrong page"
    driver.back()
    time.sleep(5)
    url = driver.current_url
    assert 'status_codes' in url, "wrong page"
    status_code_500=driver.find_element(By.XPATH,'(//ul/li)[4]/a').click()
    time.sleep(5)
    url = driver.current_url
    assert '500' in url, 'wrong page'
    driver.back()
    time.sleep(5)
    url = driver.current_url
    assert 'status_codes' in url, "wrong page"

finally :
    time.sleep(4)
    driver.quit()