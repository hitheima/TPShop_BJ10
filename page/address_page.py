from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class AddressPage(BaseAction):

    # 收货人地址 - 新建地址
    new_address_button = By.ID, "com.tpshop.malls:id/add_address_btn"

    # 点击 新建地址
    def click_new_address(self):
        self.click(self.new_address_button)
