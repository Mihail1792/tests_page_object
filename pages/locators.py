"""
Здесь находятся селекторы
Каждый класс соответствует каждому классу PageObject

Основная идея PageObject состоит в том, что каждую страницу веб-приложения можно описать в виде объекта класса.
Способы взаимодействия пользователя со страницей можно описать с помощью методов класса.
В идеале тест, который будет использовать Page Object, должен описывать бизнес-логику тестового сценария и
скрывать Selenium-методы взаимодействия с браузером и страницей. При изменениях в верстке страницы не
придется исправлять тесты, связанные с этой страницей. Вместо этого нужно будет поправить только класс,
описывающий страницу.
"""

from selenium.webdriver.common.by import By


# теперь каждый селектор — это пара: как искать и что искать.
class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")  # ссылка на логин


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")  # форма логина
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")  # форма регистрации
