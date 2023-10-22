from selenium.webdriver.common.by import By


class DzenPageLocators:
    URL = 'http://yandex.ru'
    BTN_ENTER = By.CSS_SELECTOR, '#dzen-header div.login-button__textButtonContainer-32'
    BTN_ENTER_FOR_ID = By.CSS_SELECTOR, '#tooltip-0-1 div.login-content__yaButtonWrapper-15'
