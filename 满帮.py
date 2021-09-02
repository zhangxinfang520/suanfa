# -*- coding:utf-8 -*-
#@Time : 2021/9/1 19:16
#@Author: zxf_要努力
#@File : 满帮.py
import math
import sys
from time import time, sleep


def dec(fuc):
    def w():
        start = time()
        res = fuc()
        print(res)
        end = time() - start
        print(end)
        return res
    return w

@dec
def get_all_path(n=11):
    def backtrack(i,j):
        if i == n-1 and j == n-1:
            return 1
        if i >= n or j >=n:
            return 0
        res = backtrack(i+1,j) + backtrack(i,j+2)
        return res
    a = backtrack(0,0)
    return a


def get_abs_2(n=2):
    res = 1.
    while abs( res*res - n) > 0.000001:
        res = 0.5*(res + n/res)
    return res

if __name__ == "__main__":
    # 读取第一行的n
    #n = int(sys.stdin.readline().strip())
    res = get_all_path()
    # print(len(res))
    #print("%6f"%res)
    # print(abs(-2))
    # print(math.sqrt(2)-res)
    print(res)


