import pytest

from page_objects.login_page import LoginPage
from page_objects.logged_in_successfully_page import LoggedInSuccessfullyPage


class TestPositivesScenarios:

    @pytest.mark.login
    @pytest.mark.positive
    def test_login(self, driver):

        login_page = LoginPage(driver)
        login_page.load()
        login_page.execute_login('student', 'Password123')

        logged_in_page = LoggedInSuccessfullyPage(driver)
        assert logged_in_page.current_url == logged_in_page.url
        assert logged_in_page.header_text == 'Logged In Successfully'
        assert logged_in_page.is_logout_button_displayed()

        #
        #
        # driver.get('https://practicetestautomation.com/practice-test-login/')
        #
        # # "//input[@id='username']"
        # # "//input[@id='password']"
        # # "//button[@id='submit']"
        #
        # # Type username student into Username field
        # username_field = driver.find_element(By.ID, 'username')
        # username_field.send_keys('student')
        #
        # # Type password Password123 into Password field
        # password_field = driver.find_element(By.NAME, 'password')
        # password_field.send_keys('Password123')
        #
        # # Push Submit button
        # submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
        # submit_button.click()
        #
        # # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        # actual_url = driver.current_url
        # assert actual_url == 'https://practicetestautomation.com/logged-in-successfully/'
        #
        # # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        # # log_in_successfully_text_locator = "//h1[@class='post-title']"
        # header = driver.find_element(By.TAG_NAME, 'h1')
        # actual_text = header.text
        # assert actual_text == 'Logged In Successfully'
        #
        # # Verify button Log out is displayed on the new page
        # logout_button = driver.find_element(By.LINK_TEXT, 'Log out')
        # assert logout_button.is_displayed()
