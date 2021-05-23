# -*- coding:utf-8 -*-
#@Time : 2021-05-12 13:44
#@Author: zxf_要努力
#@File : 322_零钱问题.py
'''
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
如果没有任何一种硬币组合能组成总金额，返回 -1。
你可以认为每种硬币的数量是无限的

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
输入：coins = [2], amount = 3
输出：-1
输入：coins = [1], amount = 1
输出：1
输入：coins = [1], amount = 2
输出：2
'''
from typing import List


class Solution:

    '''暴力求解法'''
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(n):
            if n==0:return 0
            if n <0:return -1
            res = float('inf')
            for coin in coins:
                subproblem = dp(n-coin)
                #子问题无解 跳过
                if subproblem ==-1: continue
                res = min(res,1+subproblem)
            return res if res!=float('inf') else -1
        return dp(amount)
    #带备忘录求解 就是消除重叠子问题
    def coinChange1(self,coins: List[int], amount: int):
        memo =dict()
        def dp(n):
            if n in memo:return memo[n]
            #base case
            if n == 0:return 0
            if n < 1 :return -1
            res = float('inf')
            for coin in coins:
                subproblem = dp(n-coin)
                if subproblem ==-1:continue
                res = min(res,1+subproblem)
            memo[n] = res if res!=float('inf') else -1
            return memo[n]
        return dp(amount)
    #自定向上的求解
    def coinChange2(self,coins:List[int],amount:int):
        result = list()
        for _ in range(amount+1):
            result.append(amount+1)
        #base case
        result[0] = 0
        # 外层for 循环在遍历所有状态的所有取值
        for i in range(len(result)):
            for coin in coins:
                #子问题无解 跳过
                if(i - coin < 0):continue
                result[i] = min(result[i],1+result[i-coin])
        print(result)
        return -1 if result[amount]==amount+1 else result[amount]






coins = [1, 2, 5]
amount = 11
print(Solution().coinChange2(coins, amount))