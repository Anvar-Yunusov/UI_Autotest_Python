from selenium.webdriver.common.by import By


class FolderPageLocators:
    URL = f'https://disk.yandex.ru/client/disk/'
    BTN_CREATE = By.CSS_SELECTOR, "#app .create-resource-popup-with-anchor"
    FILE_CREATE_BTN = By.CSS_SELECTOR, ".file-icon_doc"
    INPUT_NAME_FILE = By.CSS_SELECTOR, "body div.confirmation-dialog__content form input"
    NAME_FILE = "test_files"
    BTN_SAVE_DIALOG = By.CSS_SELECTOR, "body div.confirmation-dialog__footer button"
    CONTENT = By.CSS_SELECTOR, "#app .listing_completed"
    EXPECTED_NAME_FILE = "test_files.docx"
    MENU = By.CSS_SELECTOR, '#app .legouser__current-account.i-bem'
    BTN_EXIT = By.XPATH, "//span[@class = 'menu__text'][text() = 'Выйти']"
