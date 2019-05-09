from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 首页 - 我的
    mine_button = By.XPATH, "//*[@text='我的' and @resource-id='com.tpshop.malls:id/tab_txtv']"

    # 点击 我的
    def click_mine(self):
        self.click(self.mine_button)
