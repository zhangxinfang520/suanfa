# -*- coding:utf-8 -*-
#@Time : 2021-04-26 19:30
#@Author: zxf_要努力
#@File : asda.py
import copy
a = [1,2,[3,4]]
b = a.copy()
print(id(a))
print(id(b))
a[2][1] = 6
print(a,b)
