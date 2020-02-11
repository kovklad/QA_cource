from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    xelm = browser.find_element_by_css_selector("#treasure")
    x=xelm.get_attribute("valuex")
    print(x)
    y=calc(x)

    ans = browser.find_element_by_css_selector("#answer")
    ans.send_keys(y)
    che = browser.find_element_by_css_selector("#robotCheckbox")
    che.click()
    che2 = browser.find_element_by_css_selector("#robotsRule")
    che2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()