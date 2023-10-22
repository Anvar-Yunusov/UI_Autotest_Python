from selenium.webdriver.common.by import By


class PassportAuthPageLocators:
    URL = "https://passport.yandex.ru/"
    BTN_MAIL = By.CSS_SELECTOR, ".Button2_checked"
    INPUT_LOGIN = By.ID, "passp-field-login"
    LOGIN = "anwar-qa"
    BTN_ENTER = By.ID, "passp:sign-in"
    INPUT_PASSWORD = By.ID, "passp-field-passwd"
    PASSWORD = "Test_qa_automation"
