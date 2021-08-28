# -*- coding:utf-8 -*-
#@Time : 2021/8/25 19:20
#@Author: zxf_要努力
#@File : b站.py

#股票交易

import sys
#
# if __name__ == '__main__':
#     prices = list(map(int,sys.stdin.readline().strip().replace("[","").replace("]","").split(",")))
#     fee = int(sys.stdin.readline().strip())
#     #prices, fee = [1,3,7,5,10,3], 6
#     dp_1_0,dp_1_1 = 0, float('-inf')
#     for price in prices:
#         temp = dp_1_0
#         dp_1_0 = max(dp_1_0, dp_1_1 + price-fee)
#         dp_1_1 = max(dp_1_1,dp_1_0 + price-fee)
#     print(dp_1_0)

#获取本次分配的scores
def get_max(dp,a_list):
    score = 0
    for i in range(len(a_list)):
        score += dp[i] * a_list[i]
    return score

#判断是否 分为了k个 子数组
def is_valid(dp,k):
    if len(set(dp)) != k:
        return False
    else:
        return True

def get_max_scourse(n, k, a_list):
    dp = [0] * n

    def backtrack(idx):
        if idx == n and is_valid(dp,k):
            return get_max(dp,a_list)
        #这个是分配玩了但是没有分为k组
        if idx == n:
            return float('-inf')
        res = float('-inf')
        #贪心 为了一个数分配1到k
        for i in range(1,k+1):
            #为当前数分配
            dp[idx] = i
            #分配下一个数
            res = max(res, backtrack(idx+1) )
            #撤销分配
            dp[idx] = 0
        return res
    res = backtrack(0)
    return res




#score 求解
if __name__ == '__main__':
    n, k = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    a_list = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    print(get_max_scourse(n, k, a_list))
