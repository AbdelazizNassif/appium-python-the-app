from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class VerifyPhone(BasePage):
    # Locators
    waiting_message = (By.XPATH, "//*[@content-desc='waiting']")

    # Actions
    def get_waiting_message(self):
        return self.locate_element(*self.waiting_message).text
