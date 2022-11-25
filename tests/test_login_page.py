"""
Здесь собираются тесты. Берём методы и поля класса страницы, к примеру main_page.py и
вызываем их здесь
Для каждой страницы свой файл test_some_page.py
"""
import pytest

from pages.login_page import LoginPage


def test_guest_should_be_login_url(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_login_url()  # реализуем проверку, что подстрока "login" есть в текущем url браузера.


def test_guest_should_be_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()  # есть ли форма входа


def test_guest_should_be_register_form(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()  # есть ли форма регистрации
