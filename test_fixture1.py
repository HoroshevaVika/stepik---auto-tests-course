from selenium import webdriver

# Рассмотрим два примера: создание экземпляра браузера и его закрытие только один раз для всех 
# тестов первого тест-сьюта и создание браузера для каждого теста во втором тест-сьюте. 

link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(cls):
        print("\nstart browser for test suite..")
        cls.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        print("quit browser for test suite..")
        cls.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector(".basket-mini .btn-group > a")

# Данные и кэш, оставшиеся от запуска предыдущего теста, могут влиять на результаты выполнения следующего теста, 
# поэтому лучше всего запускать отдельный браузер для каждого теста, чтобы тесты были стабильнее. (т.е. вариант второго тест-сьюта)
# К тому же если вдруг браузер зависнет в одном тесте, то другие тесты не пострадают, если они запускаются каждый в 
# собственном браузере.

# Минусы запуска браузера на каждый тест: каждый запуск и закрытие браузера занимают время, 
# поэтому тесты будут идти дольше. Возможно, вы захотите оптимизировать время прогона тестов, 
# но лучше это делать с помощью других инструментов, которые мы разберём в дальнейшем.

#Обычно такие фикстуры переезжают вместе с тестами, написанными с помощью unittest, 
# и приходится их поддерживать, но сейчас все пишут более гибкие фикстуры @pytest.fixture, 
# которые мы рассмотрим в следующем шаге. 

