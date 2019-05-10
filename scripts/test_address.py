from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):

        self.driver = init_driver()
        print(self.driver.capabilities)
        self.page = Page(self.driver)

    def test_address(self):
        self.page.home.click_mine()
        if not self.page.mine.is_login():
            # 登录
            self.page.mine.click_login_and_signup()
            self.page.login.input_phone("xxx")
            self.page.login.input_password("xxx")
            self.page.login.click_login()

        # 点击收货地址
        # 做收货地址功能

