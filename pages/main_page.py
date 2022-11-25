"""Здесь описывается объект страницы"""
import time
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Ссылка для входа не представлена"
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        time.sleep(1)

    def should_be_login_link(self):
        # так пишутся ассерты
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Ссылка для входа не представлена"










    # # тест валится, тк такого селектора нет "#login_link_invalid"
    # def should_be_login_link(self):
    #     # так пишутся ассерты
    #     assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

    # def should_be_login_link(self):
    #     self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")



# link = "http://selenium1py.pythonanywhere.com/"
#
#
# def go_to_login_page(self):
#     login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()
#     time.sleep(4)
#
#
# def test_guest_can_go_to_login_page(browser):
#     browser.get(link)
#     go_to_login_page(browser)
