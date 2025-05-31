from pages.the_app_splash import TheAppSplash
from pages.picker_page import PicekrPage
from pages.android_popups import AndroidPopups
from pages.verify_phone import VerifyPhone


class TestDropdownList:

    def test_selecting_from_dropdown(self, driver):
        the_app_splash = TheAppSplash(driver)
        the_app_splash.click_picker_demo()
        picker = PicekrPage(driver)
        picker.select_month("March")
        assert "March" == picker.get_selected_month()
        picker.select_day("5")
        assert "5" == picker.get_selected_day()
