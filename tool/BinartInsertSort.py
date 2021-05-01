# -*- coding:utf-8 -*-
#@Time : 2021-04-26 15:03
#@Author: zxf_要努力
#@File : BinartInsertSort.py
from typing import List


def BinartInsertSort(R:List,target:int):
    n = len(R)
    if target > R[-1]:
        return n
    low = 0
    high = n-1
    ans = -1
    while low <= high:
        mid = (low+high)//2
        if R[mid] >= target:
            high = mid - 1
            ans = mid
        else :
            low = mid + 1

    return ans

a = [1, 2, 3, 4, 4, 5, 5, 6, 7]
target = 5
print(BinartInsertSort(a, target))


