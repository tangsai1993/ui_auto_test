# -*- encoding: utf-8 -*-
"""
@File    : data_loc.py
@Time    : 2021-01-03 10:07
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
"""各个元素的地址存放"""

#登录功能元素定位

login_1 = ('xpath',"//div[@class='iframe_header']//span[text()='登录']")
login_2 = ('xpath',"//div[@class='el-dialog__body']//div/p[text()='帐号密码登录']")
login_3 = ('xpath',"//input[@placeholder='请输入手机号码']")
login_4 = ('xpath',"//input[@placeholder='请输入密码']")
login_5 = ('xpath',"//span[text()='立即登录']")
login_6 = ("xpath", "//p[@class='el-message__content']")

#个人中心元素定位
myself_1=('xpath',"//div/span/div/img")
myself_2=('xpath','//*[@class="el-dropdown-menu el-popper tw-dropdown-menu"]/a[1]/li')