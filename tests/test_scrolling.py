from pages.the_app_splash import TheAppSplash
from pages.picker_page import PicekrPage
from pages.android_popups import AndroidPopups
from pages.verify_phone import VerifyPhone


class TestScrolling:

    def test_scrolling(self, driver):
        the_app_splash = TheAppSplash(driver)
        the_app_splash.scroll_till_verify_phone_is_visible()
        the_app_splash.click_verify_phone_number()
        android_popups = AndroidPopups(driver)
        android_popups.click_allow()
        verify_phone = VerifyPhone(driver)
        assert "waiting to receive a verification text message with the correct code. (hint: it's 123456)" in verify_phone.get_waiting_message().lower()



