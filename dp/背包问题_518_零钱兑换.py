# -*- coding:utf-8 -*-
#@Time : 2021-05-23 10:22
#@Author: zxf_要努力
#@File : 背包问题_518_零钱兑换.py
from typing import List

'''给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。
假设每一种面额的硬币有无限个。


输入: amount = 5, coins = [1, 2, 5]
输出: 4
解释: 有四种方式可以凑成总金额:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

输入: amount = 3, coins = [2]
输出: 0
解释: 只用面额2的硬币不能凑成总金额3。

输入: amount = 10, coins = [10] 
输出: 1
'''
'''
背包问题
memo[i][j] 代表 只使用前 i 个银币的面值，如想凑出金额j，有dp[i][j]种凑法

base case dp[0][...] = 0 ，dp[...][0] = 1 如果不使用任何的银币 是无法凑出任何金额
如果需要凑出的金额为 0 第一列都为1（无为而治）

我们最终想得到的答案就是 memo[N][amount]，其中 N 为 coins 数组的大小

状态选择 ： 只有两种 加不加硬币
首先要判断 j 是够能容这个面值的银币 j - coins[i-1] 
加 memo[i][j] = memo[i-1][j] + memo[i][j-coins[i-1]]
不加 memo[i][j] = memo[i-1][j]
'''


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
         n = len(coins)
         memo = [[0]*(amount+1) for _ in range(n+1)]
         for i in range(n+1):
             memo[i][0] = 1
         for i in range(1,n+1):
             for j in range(1,amount+1):
                 if j < coins[i-1]:
                     memo[i][j] = memo[i-1][j]
                 else:
                     memo[i][j] = memo[i-1][j]+memo[i][j-coins[i-1]]
         return memo[n][amount]

    def change1(self, amount: int, coins: List[int]):
        n = len(coins)
        memo = [0]*(amount+1)
        memo[0] = 1
        for i in range(0,n):
            for j in range(1,amount+1):
                if j - coins[i] >= 0:
                    memo[j] = memo[j] + memo[j-coins[i]]

        return memo[amount]

amount = 5
coins = [1, 2, 5]
print(Solution().change1(amount, coins))

