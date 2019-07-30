import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

# Фикстура browser, которая будет создавать объект WebDriver. 
# Этот объект мы сможем использовать в тестах для взаимодействия с браузером
@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

# Рекомендуем также выносить очистку данных и памяти в фикстуру, 
# вместо того чтобы писать это в шагах теста: финализатор выполнится даже в ситуации, когда тест упал с ошибкой.

class TestMainPage1(object):
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")