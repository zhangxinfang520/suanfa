# encoding: utf-8
"""
@author: zxf_要努力
@file: 美团1.py
@time: 2022/3/26 16:06
"""

import heapq
import sys
def get_mid_from_single(nums):
    return heapq.nsmallest(len(nums)//2+1,nums)[-1]

def get_mid(n, result):
    keys = [i for i in range(1,n+1) if i % 2 == 1 ]
    res = 0
    for key in keys:
        begin = 0
        while begin + key <= n:
            res += get_mid_from_single(result[begin:begin+key])
            begin += 1
    return res



if __name__ == '__main__':
    n = int(sys.stdin.readline())
    matrix = list(map(int, sys.stdin.readline().strip().split(" ")))
    # print(get_mid(n, matrix))
    get_mid(n,matrix)
