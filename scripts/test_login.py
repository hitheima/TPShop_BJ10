from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page
import pytest


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_data("login_data", "test_login"))
    def test_login(self, args):
        phone = args["phone"]
        password = args["password"]
        expect = args["expect"]

        # 首页 - 我的
        self.page.home.click_mine()
        # 我的 - 登录/注册
        self.page.mine.click_login_and_signup()
        # 登录 - 输入用户名
        self.page.login.input_phone(phone)
        # 登录 - 输入密码
        self.page.login.input_password(password)
        # 登录 - 点击登录
        self.page.login.click_login()
        assert self.page.login.is_toast_exits(expect)
