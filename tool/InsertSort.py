# -*- coding:utf-8 -*-
#@Time : 2021-04-26 14:50
#@Author: zxf_要努力
#@File : InsertSort.py
from typing import List


def InserSort(R:List):
    n = len(R)
    for i in range(1,n):
        temp = R[i]
        j = i-1
        while (j>=0) and temp < R[j]:
            R[j+1] = R[j]
            j -= 1
        R[j+1] = temp
    return R

sort_list = [6,4,5,7,1,2,3,4,5]
print(InserSort(sort_list))