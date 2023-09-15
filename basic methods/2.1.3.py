from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/math.html" 

    browser = webdriver.Chrome() # 114
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    time.sleep(1)
    # Отправляем заполненную форму
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Ввести ответ в текстовое поле
    input_answre = browser.find_element(By.ID, "answer")
    input_answre.send_keys(y)
    time.sleep(1)

    # checkbox
    chesck_find = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    chesck_find.click()
    time.sleep(1)

    # radiobutton
    selected_padio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    selected_padio.click()
    time.sleep(1)

    # submit
    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
