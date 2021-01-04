# -*- encoding: utf-8 -*-
"""
@File    : base.py
@Time    : 2020-12-28 21:30
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
from selenium import webdriver
from data import data_loc
class Login_base():

    def __init__(self,driver):
        """
        :param driver: 把Basepage封装的driver传入
        """
        self.driver=driver
        self.driver.click_element(data_loc.login_1)
        self.driver.click_element(data_loc.login_2)
        self.driver.input_text(data_loc.login_3,'13524280695')
        self.driver.input_text(data_loc.login_4,'1993tangsai')
        self.driver.click_element(data_loc.login_5)