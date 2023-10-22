import time

from locators.passport_auth_page_locators import PassportAuthPageLocators
from pages.base_page import BasePage


class PassportAuthPage(BasePage):

    def authorization(self):
        self.is_visible_element(PassportAuthPageLocators.BTN_MAIL).click()
        self.is_visible_element(PassportAuthPageLocators.INPUT_LOGIN).send_keys(PassportAuthPageLocators.LOGIN)
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        # так как яндекс есть защита на бота
        time.sleep(2)
        self.is_visible_element(PassportAuthPageLocators.BTN_ENTER).click()
        self.is_visible_element(PassportAuthPageLocators.INPUT_PASSWORD).send_keys(PassportAuthPageLocators.PASSWORD)
        self.is_visible_element(PassportAuthPageLocators.BTN_ENTER).click()
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        time.sleep(3)




