import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class RegionPage(BaseAction):

    # 选择城市的特征
    city_feature = By.ID, "com.tpshop.malls:id/tv_city"

    # 确定按钮
    commit_button = By.XPATH, "//*[@text='确定']"

    # 选择地区 - 确定
    def click_commit(self):
        self.click(self.commit_button)

    # 选择地区 - 选择四个区域（省、市、区、镇）
    def click_region(self):
        for i in range(4):
            self.click_city()

    # 选择地区 - 随机选择一个城市
    def click_city(self):
        # 列表 - 所有的城市的元素
        cities = self.find_elements(self.city_feature)
        # 当前的列表范围内的一个随机下标
        city_index = random.randint(0, len(cities) - 1)
        # 去除对应的随机城市，然后进行点击
        cities[city_index].click()