from selenium import webdriver
from selenium.webdriver.support.ui import Select

# Открыть страницу
#link = "http://suninjuly.github.io/selects1.html" 
link = "http://suninjuly.github.io/selects2.html"

browser = webdriver.Chrome()
browser.get(link)

# Считать значение x 
num1 = browser.find_element_by_id('num1')
x = num1.text

# Считать значение y
num2 = browser.find_element_by_id('num2')
y = num2.text

# Расcчитать значение суммы
summa = int(x) + int(y)

# Вывод результата в консоль
print(str(summa))

# Выбрать значение в выпадающем списке
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(summa)) # ищем элемент с текстом равным сумме

# Нажать на кнопку Отправить
button = browser.find_element_by_css_selector("button.btn")
button.click()
