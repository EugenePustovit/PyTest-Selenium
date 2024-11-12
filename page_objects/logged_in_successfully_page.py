from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoggedInSuccessfullyPage(BasePage):

    _url = 'https://practicetestautomation.com/logged-in-successfully/'
    __logged_in_successfully_text_locator = By.TAG_NAME, 'h1'
    __logout_button_locator = By.LINK_TEXT, 'Log out'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @property
    def url(self) -> str:
        return self._url

    @property
    def header_text(self) -> str:
        return self._get_text(self.__logged_in_successfully_text_locator)

    def is_logout_button_displayed(self) -> bool:
        return self._is_displayed(self.__logout_button_locator)
