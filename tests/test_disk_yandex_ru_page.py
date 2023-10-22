import copy

from locators.disk_yandex_ru_page_locators import DiskYandexRuPageLocators
from locators.dzen_page_locators import DzenPageLocators
from locators.folder_page_locators import FolderPageLocators
from locators.passport_auth_page_locators import PassportAuthPageLocators
from pages.disk_yandex_ru_page import DiskYandexRuPage
from pages.dzen_page import DzenPage
from pages.folder_page import FolderPage
from pages.passport_auth_page import PassportAuthPage


class TestYandexDisk:

    def test_file_created_in_folder(self, browser, logout):
        dzen_page = DzenPage(browser, DzenPageLocators.URL)
        passport_auth_page = PassportAuthPage(browser, PassportAuthPageLocators.URL)
        disk_yandex_ru_page = DiskYandexRuPage(browser, DiskYandexRuPageLocators.URL)
        folder_page = FolderPage(browser, FolderPageLocators.URL)

        dzen_page.open()
        dzen_page.go_to_authorization_page()

        passport_auth_page.authorization()

        disk_yandex_ru_page.open()
        name_folder = copy.deepcopy(disk_yandex_ru_page.name_new_folder())
        disk_yandex_ru_page.create_a_new_folder_and_name_it(name_folder)
        url = FolderPageLocators.URL+name_folder

        folder_page.open_folder(url)
        folder_page.create_a_new_file_and_name_it()
        folder_page.close_new_file()
        folder_page.check_for_a_new_file_and_its_name()

