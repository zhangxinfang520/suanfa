# -*- coding:utf-8 -*-
#@Time : 2021/9/14 9:15
#@Author: zxf_要努力
#@File : 异常抛出.py


#不通过 return 传递参数

def get_paramater(x):
    ras = Exception(x)
    raise ras


if __name__ == '__main__':

    try:
        get_paramater("zxf")
    except Exception as e:
        res = e
        print(res)