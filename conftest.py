from selenium import webdriver
import allure
import pytest

from locators.folder_page_locators import FolderPageLocators


@pytest.fixture(scope="session")
def browser():
    print('Запуск браузера для проведения тестирования')
    browser = webdriver.Chrome()
    browser.implicitly_wait(6)
    browser.maximize_window()
    yield browser
    with allure.step('Тестирование закончено, браузер закрываем'):
        browser.quit()


@pytest.fixture
def logout(browser):
    yield
    browser.find_element(*FolderPageLocators.MENU).click()
    browser.find_element(*FolderPageLocators.BTN_EXIT).click()
