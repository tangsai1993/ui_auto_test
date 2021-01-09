# -*- encoding: utf-8 -*-
"""
@File    : seting.py
@Time    : 2020-12-27 12:18
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
import os
#论坛地址
# url='http://192.168.146.128/bbs/forum.php'
#太屋网地址
url='http://www.taiwu.com'


BASE_PATH=os.path.dirname(
    os.path.dirname(__file__)
)

Picture_path=os.path.join(
    BASE_PATH,'picture'
)

Logs_path=os.path.join(
    BASE_PATH,'logs'
)

Yaml_path=os.path.join(
    BASE_PATH,'data'
)