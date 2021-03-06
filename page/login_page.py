from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class LoginPage(BaseAction):

    # 登录 - 用户名
    phone_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"
    # 登录 - 密码
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"
    # 登录 - 登录按钮
    login_button = By.ID, "com.tpshop.malls:id/btn_login"
    # 登录 - 显示密码按钮
    view_password_button = By.ID, "com.tpshop.malls:id/img_view_pwd"

    # 输入 用户名
    @allure.step(title='登录 - 输入 用户名')
    def input_phone(self, content):
        allure.attach("输入用户名", content)
        self.input(self.phone_edit_text, content)

    # 输入 密码
    @allure.step(title='登录 - 输入 密码')
    def input_password(self, content):
        allure.attach("输入密码", content)
        self.input(self.password_edit_text, content)

    # 点击 登录
    @allure.step(title='登录 - 点击 登录')
    def click_login(self):
        self.click(self.login_button)

    # 点击 显示密码
    @allure.step(title='登录 - 点击 显示密码')
    def click_view_password(self):
        self.click(self.view_password_button)

    def is_password_exits(self, password):
        """
        根据密码，判断密码是否存在
        :param password:
        :return:
        """
        password_content = By.XPATH, "//*[@text='" + password + "']"
        return self.is_feature_exits(password_content)

    def is_login_button_enabled(self):
        """
        判断 登录按钮 是否可用
        :return:
            可用：true
            不可用：false
        """
        return not self.find_element(self.login_button).get_attribute("enabled") == "false"

        # if self.find_element(self.login_button).get_attribute("enabled") == "false":
        #     return not self.find_element(self.login_button).get_attribute("enabled") == "false"
        # else:
        #     return not self.find_element(self.login_button).get_attribute("enabled") == "false"

        # if self.find_element(self.login_button).get_attribute("enabled") == "false":
        #     return False
        # else:
        #     return True

