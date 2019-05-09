from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 登录 - 用户名
    phone_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"
    # 登录 - 密码
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"
    # 登录 - 登录按钮
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    # 输入 用户名
    def input_phone(self, content):
        self.input(self.phone_edit_text, content)

    # 输入 密码
    def input_password(self, content):
        self.input(self.password_edit_text, content)

    # 点击 登录
    def click_login(self):
        self.click(self.login_button)
