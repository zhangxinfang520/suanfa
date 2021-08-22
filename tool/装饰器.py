# -*- coding:utf-8 -*-
#@Time : 2021/8/22 13:17
#@Author: zxf_要努力
#@File : 装饰器.py
'''
装饰器：就是可以让的其他函数在不改变任何代码内容的情况下，来增加函数功能
'''
#装饰器
from time import time,sleep


def run_time(func):
    print(20)
    def run(*args,**kwargs):
        start = time()
        func(*args,**kwargs)
        cost_time = time() - start
        print("fuc one run time %d"%cost_time)
    return run


@run_time
def fuc_one(a):
    print(a)
    sleep(10)


if __name__ == '__main__':
    fuc_one(10)