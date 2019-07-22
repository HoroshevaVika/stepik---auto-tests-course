from selenium import webdriver
import os

# Открыть страницу
link = " http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

# Ввести имя
firstname = browser.find_element_by_css_selector('[name="firstname"]')
firstname.send_keys("Vika")

# Ввести фамилию
lastname = browser.find_element_by_css_selector('[name="lastname"]')
lastname.send_keys("Lastname")

# Ввести email
email = browser.find_element_by_css_selector('[name="email"]')
email.send_keys("email@mail.ru")

# Найти кнопку загрузки файлов
file_btn = browser.find_element_by_id('file')
file_btn.click()

# Выбираем нужный файл
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
file_btn.send_keys(file_path)

# Нажать на кнопку Отправить
button = browser.find_element_by_css_selector("button.btn")
button.click()


