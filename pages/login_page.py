from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    # реализуйте проверку на корректный url адрес
    def should_be_login_url(self):
        current_url = self.browser.current_url  # получаем  url страницы
        assert "login" in current_url, f"Подстроки 'login' нет в текущем url браузера, текущий url: {current_url}, "

    # реализуйте проверку, что есть форма логина
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма для входа отсутствует"

    # реализуйте проверку, что есть форма регистрации на странице
    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма для регистрации отсутствует"
