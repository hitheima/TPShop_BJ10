import random
import time

import allure
from allure.constants import AttachmentType
from selenium.webdriver.common.by import By

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page
import pytest


def random_password():
    password = ""
    for i in range(8):
        password += str(random.randint(0, 9))
    return password


def run_test_show_password_times(count):
    temp_list = list()
    for i in range(count):
        temp_list.append(random_password())
    return temp_list

class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    # @pytest.mark.parametrize("password", run_test_show_password_times(2))
    # def test_show_password(self, password):
    #
    #     self.page.home.click_mine()
    #     self.page.mine.click_login_and_signup()
    #     self.page.login.input_password(password)
    #
    #     # 证明 输入的密码不存在
    #     if self.page.login.is_password_exits(password):
    #         raise Exception("密码刚刚输入，就是能找到，不符合需求")
    #
    #     self.page.login.click_view_password()
    #     time.sleep(1)
    #     allure.attach("截图：", self.driver.get_screenshot_as_png(), AttachmentType.PNG)
    #     assert self.page.login.is_password_exits(password)

    # @pytest.mark.parametrize("args", analyze_data("login_data", "test_login_miss_part"))
    # def test_login_miss_part(self, args):
    #     phone = args["phone"]
    #     password = args["password"]
    #
    #     self.page.home.click_mine()
    #     self.page.mine.click_login_and_signup()
    #     self.page.login.input_phone(phone)
    #     self.page.login.input_password(password)
    #
    #     assert not self.page.login.is_login_button_enabled()
    #
    #     # if self.page.login.is_login_button_enabled():
    #     #     assert not True
    #     # else:
    #     #     assert not False

    # @pytest.mark.parametrize("args", analyze_data("login_data", "test_login"))
    # def test_login(self, args):
    #     phone = args["phone"]
    #     password = args["password"]
    #     expect = args["expect"]
    #
    #     # 首页 - 我的
    #     self.page.home.click_mine()
    #     # 我的 - 登录/注册
    #     self.page.mine.click_login_and_signup()
    #     # 登录 - 输入用户名
    #     self.page.login.input_phone(phone)
    #     # 登录 - 输入密码
    #     self.page.login.input_password(password)
    #     # 登录 - 点击登录
    #     self.page.login.click_login()
    #     assert self.page.login.is_toast_exits(expect)
