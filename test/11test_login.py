# -*- encoding: utf-8 -*-
"""
@File    : test_login.py
@Time    : 2020-12-27 12:40
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
"""登录自动化测试"""
from conf.seting import url
from until.webkey import Webkey
import pytest
import time
import allure
import os


# class Test_login:
#     def setup(self):
#         self.driver = Webkey()
#         self.driver.openbrower()
#         self.driver.get_url(url)
#
#     def teardown(self):
#         self.driver.closebr()

def test_login(browser):
    browser.get('http://192.168.168.128/bbs/forum.php')
    browser.maximize_window()
    with allure.step("step1：点击登录"):
        # self.driver.click('//button/em')
        browser.find_element_by_xpath('//button/em').click()
    time.sleep(1)
    # self.driver.intoiframe('//*[@name="login"]')

    with allure.step("step2：输入账号"):
        # self.driver.input('//div[@class="rfm"]//input[@name="username"]', 'tangsai01')
        browser.find_element_by_xpath('//div[@class="rfm"]//input[@name="username"]').send_keys('tangsai01')
    with allure.step("step3：输入密码"):
        # self.driver.input('//div[@class="rfm"]//input[@type="password"]', '123456')
        browser.find_element_by_xpath('//div[@class="rfm"]//input[@type="password"]').send_keys('123456')
    with allure.step("step4：点击进行登录"):
        # self.driver.click("//button[@name='loginsubmit']/strong")
        browser.find_element_by_xpath("//button[@name='loginsubmit']/strong").click()
    time.sleep(5)


    assert browser.title =='None'


if __name__ == '__main__':
    pytest.main(['test_login.py','-s','--alluredir','../report/tmp1'])
    os.system(('allure serve ../report/tmp1'))
