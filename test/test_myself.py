# -*- encoding: utf-8 -*-
"""
@File    : test_myself.py
@Time    : 2021-01-03 10:32
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
from until.basepage import BasePage
from until.base_login import Login_base
from conf.seting import url
from data import data_loc
from common.real_yaml import reyaml
import time
import pytest
import os
import allure
class Test_myself():

    def setup(self):
        self.driver=BasePage()
        self.driver.open_brower_url(url)
        Login_base(self.driver)

    def teardown(self):
        self.driver.close_brower()
    def test_myself(self):
        with allure.step('step1:点击头像'):
            self.driver.click_element(data_loc.myself_1)
        with allure.step('step2:点击个人中心'):
            self.driver.click_element(data_loc.myself_2)
        with allure.step('step3:获取断言'):
            ele_text=self.driver.get_ele_text(data_loc.myself_3)
        assert '用户' in ele_text




if __name__ == '__main__':
    pytest.main(['test_myself.py', '-s', '--alluredir', '../report/tmp4'])
    os.system(('allure serve ../report/tmp4'))