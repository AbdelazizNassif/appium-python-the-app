from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TheAppSplash(BasePage):
    # Locators
    picker_demo = (By.XPATH, "//*[@text='Picker Demo']")
    verify_phone_number = (By.XPATH, "//*[@text='Verify Phone Number']")

    # Actions
    def click_picker_demo(self):
        self.locate_element(*self.picker_demo).click()

    def scroll_till_verify_phone_is_visible(self):
        self.scroll_till_text_is_visible("Verify Phone Number")

    def click_verify_phone_number(self):
        self.locate_element(*self.verify_phone_number).click()
