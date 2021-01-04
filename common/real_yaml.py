# -*- encoding: utf-8 -*-
"""
@File    : real_yaml.py
@Time    : 2021-01-03 10:04
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""

import yaml

def reyaml():
    with open('../data/data.yaml','r',encoding='utf-8') as f:
        data=f.read()
        data=yaml.load(data)
        redata=data['login']
        redata=redata[0]
        redata=redata['case']
    # print(redata)
    # for resdata in redata:
    #     resdata=list(resdata.values())[0]
    #     print(resdata)
    return redata

if __name__=='__main__':
    reyaml()
