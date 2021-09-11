# -*- coding:utf-8 -*-
#@Time : 2021/9/10 18:24
#@Author: zxf_要努力
#@File : 网易3.py
import sys

def get_loc(board,C):
    #过道两边 不影响 就是 2,3 可以相邻

    return False

if __name__ == "__main__":
    # 读取第一行的n
    N, C = list(map(int,sys.stdin.readline().strip()))
    line = sys.stdin.readline().strip()
    dp = [["."]*6 for _ in range(N)]
    for i in range(N):
        temp = sys.stdin.readline().strip().split("|")
        left,right = temp[0],temp[-1]
        temp = left + right
        for j in range(len(temp)):
            dp[i][j] = temp[j]
    if not get_loc(dp,C):
        print("FAILED")
