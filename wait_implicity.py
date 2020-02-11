from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    pr = browser.find_element_by_css_selector("#price")
    pri = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )
    button = browser.find_element_by_css_selector("#book")
    button.click()

    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)

    # alert = browser.switch_to.alert
    # alert.accept()

    xel = browser.find_element_by_css_selector("#input_value")
    x=xel.text
    y=calc(x)
    ans = browser.find_element_by_css_selector("#answer")
    ans.send_keys(y)
    
    # input1 = browser.find_element_by_tag_name('input')
    # input1.send_keys("Ivan")
    # input2 = browser.find_element_by_name('lastname')
    # input2.send_keys("Petrov")
    # input3 = browser.find_element_by_name('email')
    # input3.send_keys("Smolensk@gop.ru")

    # current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    # file_path = os.path.join(current_dir, 'input.txt') 
    # fil=browser.find_element_by_css_selector('#file')
    # print(file_path)
    # # fil.click()
    # fil.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("#solve")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()