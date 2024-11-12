from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _load(self, url: str):
        self._driver.get(url)

    def _wait_until_element_is_visible(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(ec.visibility_of_element_located(locator))

    def _find(self, locator: tuple[str, str]) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple[str, str], text: str, timeout:int = 10):
        self._wait_until_element_is_visible(locator, timeout).send_keys(text)

    def _click(self, locator: tuple[str, str], timeout:int = 10):
        self._wait_until_element_is_visible(locator, timeout).click()

    def _get_text(self, locator: tuple[str, str], timeout:int = 10) -> str:
        return self._wait_until_element_is_visible(locator, timeout).text

    def _is_displayed(self, locator: tuple[str, str], timeout:int = 10) -> bool:
        try:
            return self._wait_until_element_is_visible(locator, timeout).is_displayed()
        except NoSuchElementException:
            return False

    @property
    def current_url(self) -> str:
        return self._driver.current_url



