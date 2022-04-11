# encoding: utf-8
"""
@author: zxf_要努力
@file: 拼多多.py
@time: 2022/4/10 19:14
"""
import sys

def get_begin(M,N,left,right):
    dp = [0] * (M +1)
    for value in N:
        dp[value] = 1
    if left == right:
        if dp[left] == 1:
            return -1
        else:
            return left
    else:

        for i in range(left,right+1):
            if dp[i] == 0:
                return i
        return -1


if __name__ == '__main__':
    N,M = list(map(int,sys.stdin.readline().strip().split(" ")))
    N_list = list(map(int,sys.stdin.readline().strip().split(" ")))
    q = int(sys.stdin.readline().strip())
    for _ in range(q):
        left, rigth = list(map(int, sys.stdin.readline().strip().split(" ")))
        print(get_begin(M, N_list, left, rigth))
