from selenium.webdriver.common.by import By


class DiskYandexRuPageLocators:
    URL = "https://disk.yandex.ru/client/disk"
    NAME_FOLDER = "test_folder"
    CONTENT = By.CSS_SELECTOR, '#app .listing_completed'
    BTN_CREATE = By.CSS_SELECTOR, '#app .create-resource-popup-with-anchor'
    BTN_CREATE_FOLDER = By.CSS_SELECTOR, 'body span.file-icon.file-icon_size_m.file-icon_dir_plus.create-resource-button__icon'
    INPUT_NAME_FOLDER = By.CSS_SELECTOR, 'body div.confirmation-dialog__content form input'
    BTN_SAVE_DIALOG = By.CSS_SELECTOR, 'body div.confirmation-dialog__footer button'
