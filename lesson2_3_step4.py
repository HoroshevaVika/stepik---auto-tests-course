from selenium import webdriver
import math


# Описать функцию
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу
link = " http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link) 

# Нажать кнопку
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Принять confirm
confirm = browser.switch_to.alert
confirm.accept()

# Считать значение x 
x_element = browser.find_element_by_css_selector('[id="input_value"]')
x = x_element.text

# Расcчитать значение функции
y = calc(x)

# Ввести ответ в текстовое поле
answer = browser.find_element_by_id('answer')
answer.send_keys(y)

# Нажать на кнопку Отправить
button = browser.find_element_by_css_selector("button.btn")
button.click()


