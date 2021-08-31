# -*- coding:utf-8 -*-
#@Time : 2021/8/30 19:18
#@Author: zxf_要努力
#@File : 竞技世界.py

import numpy as np

y = input() #第一行数据
y_p = input() #第二行数据

y = [int(x) for x in y.split(",")]
y_p = [int(x) for x in y_p.split(",")]

result = 0.0
'''
计算结果放入result中，并打印出来即可print(result)
recall = tp / (tp + FN)
'''
y_numpy = np.array(y)
y_p_numpy = np.array(y_p)

TP = ((y_numpy == 1) * (y_p_numpy == 1)).sum()
T = (y_numpy == 1).sum()
if (TP + T) == 0:
    result = 0.0
else:
    result = float(TP/ (T) )

print(result)