# -*- encoding: utf-8 -*-
"""
@File    : test_login1.py
@Time    : 2020-12-28 21:11
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
from until.webkey import Webkey
from conf.seting import url
import pytest
import allure
import time
import os
class Test_login:
    def setup(self):
        self.driver = Webkey()
        self.driver.openbrower()
        self.driver.get_url(url)

    def teardown(self):
        self.driver.closebr()

    def test_login(self):
        try:
            with allure.step("step1：点击登录"):
                self.driver.click('//button/em')
            time.sleep(1)

            with allure.step("step2：输入账号"):
                self.driver.input('//div[@class="rfm"]//input[@name="username"]', 'tangsai01')
            with allure.step("step3：输入密码"):
                self.driver.input('//div[@class="rfm"]//input[@type="password"]', '123456')
            with allure.step("step4：点击进行登录"):
                self.driver.click("//button[@name='loginsubmit']/strong")
            time.sleep(5)

            assert self.driver.get_title() =='None'
        except:
            self.driver.insert_img('登录失败')
            raise


if __name__ == '__main__':
    pytest.main(['test_login1.py','-s','--alluredir','../report/tmp2'])
    os.system(('allure serve ../report/tmp2'))