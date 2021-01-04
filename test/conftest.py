# -*- encoding: utf-8 -*-
"""
@File    : conftest.py
@Time    : 2020-12-27 13:30
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""

import pytest
from selenium import webdriver
import os
import allure


driver = None
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # 添加allure报告截图
        if hasattr(driver, "get_screenshot_as_png"):
            with allure.step('添加失败截图...'):
                allure.attach(driver.get_screenshot_as_png(), "失败截图", allure.attachment_type.PNG)


@pytest.fixture(scope='session')
def browser():
    global driver
    if driver is None:
        driver =webdriver.Chrome()
    yield driver
    print("打开浏览器")
    driver.quit()
