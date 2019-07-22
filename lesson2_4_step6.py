from selenium import webdriver
import math

# Описать функцию
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

# Открыть страницу
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link) 

# Нажать на бегающую кнопку
button = browser.find_element_by_class_name('trollface')
button.click()

# Переключиться на новую вкладку
new_window = browser.window_handles[1] # Нашли 2ую по счету вкладку в браузере
first_window = browser.window_handles[0] # Запомнили предыдущую вкладку на всякий случай
browser.switch_to.window(new_window) # Переключились на новую вкладку

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


