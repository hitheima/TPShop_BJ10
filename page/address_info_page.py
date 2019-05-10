from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class AddressInfoPage(BaseAction):

    # 收货地址 - 收货人
    name_edit_text = By.ID, "com.tpshop.malls:id/consignee_name_edtv"

    # 收货地址 - 手机号
    phone_edit_text = By.ID, "com.tpshop.malls:id/consignee_mobile_edtv"

    # 收货地址 - 详细地址
    address_edit_text = By.ID, "com.tpshop.malls:id/consignee_address_edtv"

    # 收货地址 - 区域
    regin_button = By.ID, "com.tpshop.malls:id/consignee_region_txtv"

    # 输入 收货人
    def input_name(self, content):
        self.input(self.name_edit_text, content)

    # 输入 收货人
    def input_phone(self, content):
        self.input(self.phone_edit_text, content)

    # 输入 收货人
    def input_address(self, content):
        self.input(self.address_edit_text, content)

    # 点击 区域
    def click_regin(self, content):
        self.input(self.regin_button, content)
