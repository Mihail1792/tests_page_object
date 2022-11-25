"""
Базовый класс, в котором опысываются методы взаимодействия для всех страниц сайта,
по типу прокидывания урлов, проверки наличия элемента, таймаутов ожидания и пр.
"""

from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import имя_исключения


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    # Теперь для всех проверок, что элемент действительно присутствует на странице, мы можем использовать этот метод.
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        # except (имя исключения):
        except NoSuchElementException:
            return False
        return True
