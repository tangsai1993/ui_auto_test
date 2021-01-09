# -*- encoding: utf-8 -*-
"""
@File    : test_login_taiwu.py
@Time    : 2020-12-30 21:11
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""

from selenium import webdriver
from until.basepage import BasePage
from conf.seting import url
from data import data_loc
from common.real_yaml import reyaml
import time
import pytest
import os
import allure
class Test_login():

    def setup(self):
        self.driver=BasePage()
        self.driver.open_brower_url(url)

    def teardown(self):
        self.driver.close_brower()
    @pytest.mark.parametrize('login_data',reyaml())
    def test_login(self,login_data):
        with allure.step("step1：点击登录按钮"):
            self.driver.click_element(data_loc.login_1)
        with allure.step("step2：点击账号登录"):
            self.driver.click_element(data_loc.login_2)
        with allure.step("step3：输入账号"):
            self.driver.input_text(data_loc.login_3, login_data['name'])
        with allure.step("step4：输入密码"):
            self.driver.input_text(data_loc.login_4, login_data['password'])
        #截图输入的账号和密码
        self.driver.save_page_shot('已输入账号密码')
        with allure.step("step5：点击立即登录"):
            self.driver.click_element(data_loc.login_5)
        with allure.step("step6：获取登录提示语"):
            ele_text = self.driver.get_ele_text(data_loc.login_6)
        try:
            assert ele_text == '登录成功'
        except:
            self.driver.save_page_shot('太屋网登录账号')
            raise

if __name__ == '__main__':
    pytest.main(['test_login_taiwu.py', '-s', '--alluredir', '../report/tmp3'])
    os.system(('allure serve ../report/tmp3'))