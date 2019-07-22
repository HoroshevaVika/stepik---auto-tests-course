from selenium import webdriver
import math

# Описать функцию
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу
link = "http://suninjuly.github.io/math.html"
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
robotsRule.click()

# Нажать на кнопку Отправить
button = browser.find_element_by_css_selector("button.btn")
button.click()
