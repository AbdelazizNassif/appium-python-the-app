from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AndroidPopups(BasePage):
    # Locators

    # Actions
    def click_allow(self):
        self.locate_element(By.XPATH, "//*[@text='Allow']").click()
