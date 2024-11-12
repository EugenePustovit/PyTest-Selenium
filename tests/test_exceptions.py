import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):

        # Open page
        driver.get('https://practicetestautomation.com/practice-test-exceptions/')

        # Click Add button
        add_button = driver.find_element(By.ID, 'add_btn')
        add_button.click()

        wait = WebDriverWait(driver, 10)
        row2_field = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@id="row2"]/input')))

        # Verify Row 2 input field is displayed
        # row2_field = driver.find_element(By.XPATH, '//div[@id="row2"]/input')
        assert row2_field.is_displayed(), 'Row2 field is not displayed'


    def test_element_not_interactable_exception(self, driver):

        # Open page
        driver.get('https://practicetestautomation.com/practice-test-exceptions/')

        # Click Add button
        add_button = driver.find_element(By.ID, 'add_btn')
        add_button.click()

        # Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row2_field = wait.until(ec.presence_of_element_located((By.XPATH, '//div[@id="row2"]/input')))

        # Type text into the second input field
        row2_field.send_keys('text')

        # Push Save button using locator By.name(“Save”)


        # Verify text saved