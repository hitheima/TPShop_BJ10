from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure

class MinePage(BaseAction):

    # 我的 - 登录/注册
    login_and_signup_button = By.XPATH, "//*[@text='登录/注册']"

    # 我的 - 设置按钮
    setting_button = By.ID, "com.tpshop.malls:id/setting_btn"

    # titlebar_标题
    titlebar_title = By.ID, "com.tpshop.malls:id/titlebar_title_txtv"

    # 收货地址的特征
    address_button = By.XPATH, "//*[@text='收货地址']"

    @allure.step(title='我的 - 点击 登录/注册')
    # 点击 登录/注册
    def click_login_and_signup(self):
        self.click(self.login_and_signup_button)

    @allure.step(title='我的 - 点击 设置按钮')
    # 点击 设置按钮
    def click_setting(self):
        self.click(self.setting_button)

    @allure.step(title='我的 - 点击 设置按钮')
    # 点击 设置按钮
    def get_titlebar_text(self):
        return self.find_element(self.titlebar_title).text

    def click_address(self):
        if self.is_feature_exist_with_scroll(self.address_button):
            self.click(self.address_button)
        else:
            raise Exception("没有找到收货地址")

    def is_login(self):
        """
        判断登录状态
        :return:
        """
        # 点击设置
        self.click_setting()
        # 如果标题为设置，则为登录成功
        is_login = self.get_titlebar_text() == '设置'
        # 返回
        self.press_back()
        return is_login



        # if self.get_titlebar_text() == "设置":
        #     return True
        # else:
        #     return False


