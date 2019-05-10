from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):

        self.driver = init_driver()
        self.page = Page(self.driver)

    def test_address(self):
        self.page.home.click_mine()
        if not self.page.mine.is_login():
            # 登录
            self.page.mine.click_login_and_signup()
            self.page.login.input_phone("13800138006")
            self.page.login.input_password("123456")
            self.page.login.click_login()

        # 点击收货地址
        self.page.mine.click_address()

        # 做收货地址功能
        
