from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoginPage(BasePage):

    _url = 'https://practicetestautomation.com/practice-test-login/'

    __username_field_locator = By.ID, 'username'
    __password_field_locator = By.NAME, 'password'
    __submit_button_locator = By.XPATH, '//button[@id="submit"]'
    __error_message_locator = By.XPATH, '//div[@id="error"]'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def load(self):
        self._load(self._url)

    def execute_login(self, username, password: str):
        self._type(self.__username_field_locator, username)
        self._type(self.__password_field_locator, password)
        self._click(self.__submit_button_locator)

    def is_error_message_displayed(self) -> bool:
        return self._is_displayed(self.__error_message_locator)

    @property
    def error_message(self) -> str:
        return self._get_text(self.__error_message_locator)




