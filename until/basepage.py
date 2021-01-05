# -*- encoding: utf-8 -*-
"""
@File    : basepage.py
@Time    : 2020-12-30 21:14
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
"""page层"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.loger import logger
from conf.seting import Picture_path
import time
import allure

logger=logger()


# 记录日志/失败截图+错误信息输出+抛出异常
class BasePage:
    # BasePage类，针对PageObjects类的二次封装
    def __init__(self):
        self.driver=None
    #打开浏览器模式
    # def open_brower_url(self,url):
    #     self.driver=webdriver.Chrome()
    #     self.driver.get(url)
    #     self.driver.maximize_window()
    #无头模式--不用打开浏览器
    def open_brower_url(self,url):
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # 无界面
        chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在报错问题
        chrome_options.add_argument('--disable-gpu')  # 禁用GPU硬件加速。如果软件渲染器没有就位，则GPU进程将不会启动。
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920,1080')  # 设置当前窗口的宽度和高度
        self.driver = webdriver.Chrome('chromedriver', options=chrome_options)
        # self.driver=webdriver.Chrome()
        self.driver.get(url)
    #关闭浏览器
    def close_brower(self):
        self.driver.quit()

    # 1.等待元素可见
    def wait_ele_visible(self,loc,timeout=20,poll_fre=0.5):
        """
        :param loc: 元素定位
        :param img_name: {页面名称_页面行为}
        :param timeout: 最长超时时间，默认以秒为单位
        :param poll_fre: 检测的间隔步长，默认为0.5s
        :return:
        查找元素用了多久？
        等待开始的时候，记录一下当前的时间，等等待结束后，再记录一次，然后计算时间差
        """
        logger.info("等待 {} 元素可见。".format(loc))
        # 等待开始的时候，记录一下当前的时间
        start_time = time.time()
        try:
            WebDriverWait(self.driver,timeout, poll_frequency=poll_fre).until(EC.visibility_of_element_located(loc))
        except:
            logger.exception("等待元素可见失效！")  # 异常信息写入日志当中
            raise
        else:
            # 等待结束后，再记录一次，然后计算时间差
            end_time = time.time()
            dif_time = int(end_time) - int(start_time)
            logger.info("等待 {} 元素时间 {}".format(loc, dif_time))

    # 2.查找元素
    def get_element(self,loc):
        logger.info("查找元素 {}。".format(loc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            logger.exception("查找元素失败！")  # 异常信息写入日志当中
            raise
        else:  # 查找成功返回ele对象
            return ele

    # 查找所有的元素
    def get_elements(self,loc):
        logger.info("查找所有元素 {}。".format(loc))
        try:
            eles = self.driver.find_elements(*loc)
        except:
            logger.exception("查找所有元素失败！")  # 异常信息写入日志当中
            raise
        else:  # 查找成功返回ele对象
            return eles

    # 3.点击 # 需要元素可见
    def click_element(self,loc,timeout=20,poll_fre=0.5):
        self.wait_ele_visible(loc,timeout,poll_fre)
        ele = self.get_element(loc)
        logger.info("点击 {} 元素。".format(loc))
        try:
            ele.click()
        except:
            logger.exception("点击元素失败！")  # 异常信息写入日志当中
            raise

    # 4.文本输入
    def input_text(self,loc,value,timeout=20,poll_fre=0.5):
        self.wait_ele_visible(loc,timeout,poll_fre)
        ele = self.get_element(loc)
        logger.info("往 {} 元素中输入文本值 {}。".format(loc, value))
        try:
            ele.send_keys(value)
        except:
            logger.exception("文本输入元素失败！")  # 异常信息写入日志当中
            raise

    # 5.获取属性  - 不一定要可见 - 没有绝对的答案
    def get_ele_attribute(self,loc,attr_name,timeout=20,poll_fre=0.5):
        self.wait_ele_visible(loc,timeout,poll_fre)
        ele = self.get_element(loc)
        logger.info("获取 {} 元素的 {} 属性。".format(loc,attr_name))
        try:
            value = ele.get_attribute(attr_name)
        except:
            logger.exception("获取元素属性值失败！")  # 异常信息写入日志当中
            raise
        else:
            logger.info("属性值为：{}".format(value))
            return value

    # 6.元素存在
    # def wait_page_element_exist(self):
    #     pass

    # 7.获取元素文本值
    def get_ele_text(self, loc,timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc,timeout, poll_fre)
        ele = self.get_element(loc)
        logger.info("获取 {} 元素的文本值。".format(loc))
        try:
            text = ele.text
        except:
            logger.exception("获取元素属性值失败！")  # 异常信息写入日志当中
            raise
        else:
            logger.info("文本值为：{}".format(text))
            return text

    # 保存截图
    def save_page_shot(self,img_name):
        """
        :param file_name:{页面名称_页面行为}
        :return:
        """

        """截图并且加入allure报告"""
        now = time.strftime("%Y-%m-%d %H-%M-%S")
        # file_path = f'../picture/{now}{img_name}.png'
        file_path = f'{Picture_path}/{now}{img_name}.png'
        #截图保存至指定目录
        self.driver.get_screenshot_as_file(file_path)
        #加入allure报告中
        with open(file_path, mode='rb') as f:
            file = f.read()
        allure.attach(file,img_name,allure.attachment_type.PNG)


if __name__ == '__main__':
    # import time
    # now = time.strftime("%Y-%m-%d %H:%M:%S")
    # print(now)
    from selenium import webdriver

    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    # 调basepage类里面的页面操作行为，实例化
    bp = BasePage(driver)
    search_loc = ("id", "kw")
    bp.input_text(search_loc, "basepage二次封装", "百度页面_搜索输入操作")
