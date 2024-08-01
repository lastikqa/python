from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    span_list = []
    browser.get('https://parsinger.ru/infiniti_scroll_2/')
    div = browser.find_element(By.XPATH, '//*[@id="scroll-container"]/div')
    for x in range(10):
        nums = browser.find_elements(By.XPATH, f"//div/p")
        for i in nums:
            num = i.text
            if num.isdigit():
                if int(num) not in span_list:
                    span_list.append(int(num))
        ActionChains(browser).move_to_element(div).scroll_by_amount(1, 500).perform()
    print(sum(span_list))