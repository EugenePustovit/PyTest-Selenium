import time

import pytest
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize('username, password, exp_error_msg',
                             [('incorrectUser', 'Password123', 'Your username is invalid!'),
                              ('student', 'incorrectPassword', 'Your password is invalid!')])
    def test_negative_login(self, driver, username, password, exp_error_msg):

        login_page = LoginPage(driver)
        login_page.load()
        login_page.execute_login(username, password)
        assert login_page.is_error_message_displayed()
        assert login_page.error_message == exp_error_msg

        # # Open page
        # driver.get('https://practicetestautomation.com/practice-test-login/')
        #
        # # Type username incorrectUser into Username field
        # username_field = driver.find_element(By.ID, 'username')
        # username_field.send_keys(username)
        #
        # # Type password Password123 into Password field
        # password_field = driver.find_element(By.NAME, 'password')
        # password_field.send_keys(password)
        #
        # # Push Submit button
        # submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
        # submit_button.click()
        #
        # time.sleep(2)
        # # Verify error message is displayed
        # error = driver.find_element(By.ID, 'error')
        # # error = driver.find_element(By.XPATH, '//div[@id="error"]')
        # assert error.is_displayed(), 'Error message is not displayed'
        #
        # # Verify error message text is Your username is invalid!
        # assert error.text == exp_error_msg, 'Error message is not as expected'


    def test_negative_username(self, driver):

        # Open page
        driver.get('https://practicetestautomation.com/practice-test-login/')

        # Type username incorrectUser into Username field
        username_field = driver.find_element(By.ID, 'username')
        username_field.send_keys('incorrectUser')

        # Type password Password123 into Password field
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('Password123')

        # Push Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button.click()

        # Verify error message is displayed
        time.sleep(2)
        error = driver.find_element(By.ID, 'error')
        assert error.is_displayed(), 'Error message is not displayed'

        # Verify error message text is Your username is invalid!
        error_msg = 'Your username is invalid!'
        assert error.text == error_msg, 'Error message is not as expected'


    def test_negative_password(self, driver):

        # Open page
        driver.get('https://practicetestautomation.com/practice-test-login/')

        # Type username student into Username field
        username_field = driver.find_element(By.ID, 'username')
        username_field.send_keys('student')

        # Type password incorrectPassword into Password field
        password_field = driver.find_element(By.NAME, 'password')
        password_field.send_keys('incorrectPassword')

        # Push Submit button
        submit_button = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button.click()

        # Verify error message is displayed
        time.sleep(2)
        error = driver.find_element(By.ID, 'error')
        assert error.is_displayed(), 'Error message is not displayed'

        # Verify error message text is Your password is invalid!
        error_msg = 'Your password is invalid!'
        assert error.text == error_msg, 'Error message is not as expected'

