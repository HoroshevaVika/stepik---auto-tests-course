from selenium import webdriver
import math
import os

# Описать функцию
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу
link = "https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

# Считать значение x 
x_element = browser.find_element_by_css_selector('[id="input_value"]')
x = x_element.text

# Расcчитать значение функции
y = calc(x)

# Вывод результата в консоль
print(y)

# Ввести ответ в текстовое поле
answer = browser.find_element_by_id('answer')
answer.send_keys(y)

# Отметить checkbox "Подтверждаю, что являюсь роботом"
robotCheckbox = browser.find_element_by_css_selector('[for="robotCheckbox"]')
robotCheckbox.click()

# Выбрать radiobutton "Роботы рулят!"
robotsRule = browser.find_element_by_css_selector('[for="robotsRule"]')
browser.execute_script("return arguments[0].scrollIntoView(true);", robotsRule)
robotsRule.click()

# Нажать на кнопку Отправить
button = browser.find_element_by_css_selector("button.btn")
button.click()

 # Выводы путей
print(os.path.abspath(__file__)) # Полный путь файла 
print(os.path.abspath(os.path.dirname(__file__))) # Путь до файла 

