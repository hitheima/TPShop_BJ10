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
        # 收货人地址页面 - 点击 新建地址
        self.page.address.click_new_address()
        # 收货地址 - 输入用户名
        self.page.address_info.input_name("张三")
        # 收货地址 - 输入手机号
        self.page.address_info.input_phone("13800138006")
        # 收货地址 - 输入详细地址
        self.page.address_info.input_address("2单元 402")


