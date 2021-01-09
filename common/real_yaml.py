# -*- encoding: utf-8 -*-
"""
@File    : real_yaml.py
@Time    : 2021-01-03 10:04
@Author  : tangsai
@Email   : 294168604@qq.com
@Software: PyCharm
"""
from conf.seting import Yaml_path
import yaml

def reyaml():
    with open(f'{Yaml_path}/data.yaml','r',encoding='utf-8') as f:
        data=f.read()
        data=yaml.load(data,Loader=yaml.FullLoader)
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
