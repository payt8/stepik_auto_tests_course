from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html" 

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")

    x = x_element.get_attribute("valuex")
    y = calc(x)
    # print(x,y)

    input_answre = browser.find_element(By.ID, "answer")
    input_answre.send_keys(y)
    time.sleep(1)

    # checkbox
    chesck_find = browser.find_element(By.ID, "robotCheckbox")
    chesck_find.click()
    time.sleep(1)

    # radiobutton
    selected_padio = browser.find_element(By.ID, "robotsRule")
    selected_padio.click()
    time.sleep(1)

    # submit
    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()
