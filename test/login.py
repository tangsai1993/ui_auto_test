# -*- encoding: utf-8 -*-
"""
@File    : login.py
@Time    : 2020-12-27 13:03
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
from conf.seting import url
from until.webkey import Webkey
import pytest
import time

driver = Webkey()
driver.openbrower()
driver.get_url(url)
driver.click('//button/em')
time.sleep(1)
driver.input('//div[@class="rfm"]//input[@name="username"]', 'tangsai01')
driver.input('//div[@class="rfm"]//input[@type="password"]', '123456')
driver.click("//button[@name='loginsubmit']/strong")
ele=driver.get_title()
print(ele)