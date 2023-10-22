import copy
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from locators.disk_yandex_ru_page_locators import DiskYandexRuPageLocators
from pages.base_page import BasePage


class DiskYandexRuPage(BasePage):

    def name_new_folder(self):
        disk_content = copy.deepcopy(self.is_visible_element(DiskYandexRuPageLocators.CONTENT).text)
        count_folder = disk_content.count(DiskYandexRuPageLocators.NAME_FOLDER)
        name_folder = DiskYandexRuPageLocators.NAME_FOLDER + f' ({count_folder})'
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        time.sleep(3)
        return name_folder

    def delete_input_text_folder(self):
        self.is_visible_element(DiskYandexRuPageLocators.INPUT_NAME_FOLDER).click()
        self.is_visible_element(DiskYandexRuPageLocators.INPUT_NAME_FOLDER).send_keys(Keys.CONTROL + 'a')
        self.is_visible_element(DiskYandexRuPageLocators.INPUT_NAME_FOLDER).send_keys(Keys.DELETE)
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        time.sleep(3)

    def create_a_new_folder_and_name_it(self, name_folder):
        self.is_visible_element(DiskYandexRuPageLocators.BTN_CREATE).click()
        self.is_visible_element(DiskYandexRuPageLocators.BTN_CREATE_FOLDER).click()
        self.delete_input_text_folder()
        self.is_visible_element(DiskYandexRuPageLocators.INPUT_NAME_FOLDER).send_keys(f'{name_folder}')
        self.is_visible_element(DiskYandexRuPageLocators.BTN_SAVE_DIALOG).click()
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        time.sleep(3)
