import time

from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class techactions:

    def generate_random_finance_word(self):
        # List of meaningful finance-related words
        finance_words = ["investment", "accounting", "bank", "capital", "finance", "tax", "budget", "audit", "stock",
                         "asset"]
        # Function to generate random finance-related word
        return random.choice(finance_words)

class basicuseraction:
    def hover(self,element_to_hover_over):
        ''' This function will require Action Chains Import'''
        # Perform the hover action
        hover = self.ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()



class testactions:

    def click_and_verify_url(self,click_element_location,url):
        try:
            time.sleep(3)
            click_element_location.click()
            WebDriverWait(self.driver, 20).until(EC.url_changes(self.driver.current_url))
        except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException):
            assert False
        else:
            # If the expected URL is reached, verify it
            assert self.driver.current_url == url

    from selenium.webdriver.common.keys import Keys

    def click_and_verify_url1(self, click_element_location, url):
        try:
            current_window_handle = self.driver.current_window_handle

            # Click the element to open the URL
            click_element_location.click()

            # Wait for a new window or tab to open
            WebDriverWait(self.driver, 20).until(lambda driver: len(driver.window_handles) > 1)

            # Switch to the new window
            for window_handle in self.driver.window_handles:
                if window_handle != current_window_handle:
                    new_window_handle = window_handle
                    self.driver.switch_to.window(new_window_handle)
                    break

            # Get the URL of the new window
            new_window_url = self.driver.current_url

            # Close the new window
            self.driver.close()

            # Switch back to the original window
            self.driver.switch_to.window(current_window_handle)

            # Verify the URL
            assert new_window_url == url

        except (
        NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException, TimeoutException):
            assert False

    def is_not_displayed(element):
        try:
            return not element.is_displayed()
        except NoSuchElementException:
            return True
