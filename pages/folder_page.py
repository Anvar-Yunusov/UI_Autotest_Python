import copy
import time

from selenium.webdriver import Keys
from locators.folder_page_locators import FolderPageLocators
from pages.base_page import BasePage


class FolderPage(BasePage):

    def open_folder(self, url):
        self.browser.get(url)
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        time.sleep(3)

    def delete_input_text_file(self):
        self.is_visible_element(FolderPageLocators.INPUT_NAME_FILE).click()
        self.is_visible_element(FolderPageLocators.INPUT_NAME_FILE).send_keys(Keys.CONTROL + 'a')
        self.is_visible_element(FolderPageLocators.INPUT_NAME_FILE).send_keys(Keys.DELETE)
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        time.sleep(3)

    def create_a_new_file_and_name_it(self):
        self.is_visible_element(FolderPageLocators.BTN_CREATE).click()
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        # так как яндекс есть защита на бота
        time.sleep(1)
        self.is_visible_element(FolderPageLocators.FILE_CREATE_BTN).click()
        self.delete_input_text_file()
        self.is_visible_element(FolderPageLocators.INPUT_NAME_FILE).send_keys(FolderPageLocators.NAME_FILE)
        self.is_visible_element(FolderPageLocators.BTN_SAVE_DIALOG).click()
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        time.sleep(3)

    def close_new_file(self):
        self.browser.switch_to.window(self.browser.window_handles[1])
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        # так как яндекс есть защита на бота
        time.sleep(3)
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def check_for_a_new_file_and_its_name(self):
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        # так как яндекс есть защита на бота
        time.sleep(3)
        folder_content = copy.deepcopy(self.is_visible_element(FolderPageLocators.CONTENT).text)
        assert len(folder_content) != 0, 'В папке нет файлов'
        assert folder_content == FolderPageLocators.EXPECTED_NAME_FILE, 'Название файла некорректное'
        print('В папке есть файл и название соответствует ожидаемому')
