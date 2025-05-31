from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage


class PicekrPage(BasePage):
    # Locators
    month_picker_dropdown = (By.XPATH, "//*[@content-desc='monthPicker']")
    selected_option = (By.ID, "android:id/text1")
    day_picker_dropdown = (By.XPATH, "//*[@content-desc='dayPicker']")

    # Actions
    def select_month(self, month_to_pick):
        dropdown = self.locate_element(*self.month_picker_dropdown)
        dropdown.click()
        self.locate_element(By.XPATH, f"//*[@text='{month_to_pick}']").click()

    def select_day(self, day_to_pick):
        dropdown = self.locate_element(*self.day_picker_dropdown)
        dropdown.click()
        self.locate_element(By.XPATH, f"//*[@text='{day_to_pick}']").click()

    def get_selected_month(self):
        dropdown_option = self.locate_element(*self.month_picker_dropdown).find_element(*self.selected_option)
        return dropdown_option.text

    def get_selected_day(self):
        dropdown_option = self.locate_element(*self.day_picker_dropdown).find_element(*self.selected_option)
        return dropdown_option.text
