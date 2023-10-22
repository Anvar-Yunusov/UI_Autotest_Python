import time

from locators.dzen_page_locators import DzenPageLocators
from pages.base_page import BasePage


class DzenPage(BasePage):
    def go_to_authorization_page(self):
        self.is_visible_element(DzenPageLocators.BTN_ENTER).click()
        self.is_visible_element(DzenPageLocators.BTN_ENTER_FOR_ID).click()
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        # так как яндекс есть защита на бота
        time.sleep(2)
