import os
import math
import time
import pyperclip as pc

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome() # 114
    browser.implicitly_wait(5)
    browser.get(link)

    js = "return arguments[0].scrollIntoView(true);"


    price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    print(price)
    if price:
        browser.find_element(By.ID, "book").click()
        
    submit = browser.find_element(By.ID, "solve")
    browser.execute_script(js, submit)  

    x = browser.find_element(By.ID, "input_value").text
    y = str(math.log(abs(12*math.sin(int(x)))))
    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    
    submit.click()
    time.sleep(1) 

    alert = browser.switch_to.alert
    time.sleep(1)
    pc.copy(alert.text.split()[-1])
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()