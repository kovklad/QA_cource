from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    xel1 = browser.find_element_by_css_selector("#num1")
    x1=xel1.text
    xel2 = browser.find_element_by_css_selector("#num2")
    x2=xel2.text
    print(x1,x2)
    y=int(x1)+int(x2)
    print(y)
    # y2='"[value="'+str(y)+'"]"'
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector('[value="'+str(y)+'"]').click()


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