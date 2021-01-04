# -*- encoding: utf-8 -*-
"""
@File    : webkey.py
@Time    : 2020-12-27 12:09
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""

"""封装浏览器操作"""
from selenium import webdriver
from conf.seting import Picture_path
import time
import allure
class Webkey:
    def __init__(self):
        self.driver=None
    def openbrower(self, br='gc'):
        if br == 'gc':
            self.driver = webdriver.Chrome()
        elif br == 'ff':
            self.driver = webdriver.Firefox()
        elif br == 'ie':
            self.driver = webdriver.Ie()
        else:
            print('浏览器暂不支持！请在此添加实现代码')
        self.driver.implicitly_wait(10)  # 隐形等待10秒
    def get_url(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def click(self, locator=None):
        self.driver.find_element_by_xpath(locator).click()

    def input(self, locator=None, value=None):
        self.driver.find_element_by_xpath(locator).send_keys(value)

    def ele(self, locator):
        self.driver.find_element_by_xpath(locator)

    def intoiframe(self, locator=None):
        ele = self.driver.find_element_by_xpath(locator)
        self.driver.switch_to.frame(ele)

    def closebr(self):
        self.driver.close()

    def alert_text(self):
        self.driver.switch_to_alert().text

    def ele(self,locator):
        self.driver.find_element_by_xpath(locator)

    def get_title(self):
        ele=self.driver.title
        return ele

    def insert_img(self, file_name):
        """截图并且加入allure报告"""
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        # file_path = f'../picture/{now}{file_name}.png'
        file_path = f'{Picture_path}/{now}{file_name}.png'
        #截图保存至指定目录
        self.driver.get_screenshot_as_file(file_path)
        #加入allure报告中
        with open(file_path, mode='rb') as f:
            file = f.read()
        allure.attach(file, file_name, allure.attachment_type.PNG)

