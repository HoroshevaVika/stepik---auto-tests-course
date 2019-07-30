import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


# Для фикстур можно задавать область покрытия фикстур. 
# Допустимые значения: “function”, “class”, “module”, “session”. 
# Соответственно, фикстура будет вызываться один раз для тестового метода, один раз для класса,
# один раз для модуля или один раз для всех тестов, запущенных в данной сессии. 

# создаем фикстуру для класса (т.е. все тесты запустятся в одном браузере)
# этот метод не рекомендуется. Лучше запускать каждый тест в своем браузере
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1(object)

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")