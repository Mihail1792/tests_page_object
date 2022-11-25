import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)

    # Неявное ожидание указывает WebDriver'у опрашивать DOM определенное количество времени,
    # когда пытается найти элемент или элементы, которые недоступны в тот момент.
    # Значение по умолчанию равно 0. После установки, неявное ожидание устанавливается
    # для жизни экземпляра WebDriver объекта.
    # browser.implicitly_wait(10)  # seconds
    yield browser

    print("\nquit browser..")
    browser.quit()


#  парсит данные из командной строки
def pytest_addoption(parser):
    # parser.addoption('--browser_name', action='store', default="chrome",
    #                  help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: de, ru or en")
# , default="en",


@pytest.fixture
def driver(request):
    language = request.config.getoption('--language')



