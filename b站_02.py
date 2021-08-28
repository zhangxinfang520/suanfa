# -*- coding:utf-8 -*-
#@Time : 2021/8/25 19:20
#@Author: zxf_要努力
#@File : b站.py

#股票交易

import sys
import copy

def get_max_scourse(n, k, a_list):
    if k == 1:
        return sum(a_list)
    rightsum = [sum(a_list[i:]) for i in range(1,n)]
    rightsum.sort(reverse=True)

    res = sum(a_list) + sum(rightsum[:k-1])
    return res



#score 求解
if __name__ == '__main__':
    n, k = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    a_list = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    print(get_max_scourse(n, k, a_list))


