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

if __name__ == '__main__':
    pytest.main(['test_myself.py', '-s', '--alluredir', '../report/tmp1'])
    os.system(('allure serve ../report/tmp1'))