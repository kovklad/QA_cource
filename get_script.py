from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # Ваш код, который заполняет обязательные поля
    xel1 = browser.find_element_by_css_selector("#input_value")
    x1=xel1.text
    # xel2 = browser.find_element_by_css_selector("#num2")
    # x2=xel2.text
    # print(x1,x2)
    y=calc(x1)
    print(y)
    browser.execute_script("window.scrollBy(0, 100);")
    # button = document.getElementsByTagName("button")[0];
    # button.scrollIntoView();
    ans = browser.find_element_by_css_selector("#answer")
    ans.send_keys(y)
    che = browser.find_element_by_css_selector("#robotCheckbox")
    che.click()
    che2 = browser.find_element_by_css_selector("#robotsRule")
    che2.click()
    # y2='"[value="'+str(y)+'"]"'
    # browser.find_element_by_tag_name("select").click()
    # browser.find_element_by_css_selector('[value="'+str(y)+'"]').click()


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