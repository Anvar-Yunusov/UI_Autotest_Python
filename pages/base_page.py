import time


class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def is_visible_element(self, locator):
        return self.browser.find_element(*locator)

    def open(self):
        self.browser.get(self.url)
        # мне известно, что ставить time.sleep() это плохая практика, но так как яндекс определяет
        # что это бот и из-за этого вылетает на авторизацию было принято решение поставить, таким образом симулировать
        # поведение человека
        # так как яндекс есть защита на бота
        time.sleep(3)
