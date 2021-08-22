# -*- coding:utf-8 -*-
#@Time : 2021-06-05 22:07
#@Author: zxf_要努力
#@File : 188_买卖股票的最佳时期IV.py
'''
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。
设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

一次交易由买入和卖出构成，至少需要两天。所以说有效的限制 k 应该不超过 n/2，
如果超过，就没有约束作用了，相当于 k = +infinity。这种情况是之前解决过的。相当于调用122的方法

'''
from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if k > (len(prices) / 2):
            return self.maxprofit_free_k(prices)
        dp = [[0] *2 for _ in range(k+1)]
        for i in range(1,k+1):
            dp[i][0] = 0
            dp[i][1] = -prices[0]
        for i in range(1,len(prices)):
            for j in range(k,0,-1):
                dp[j][0] = max(dp[j][0], dp[j][1] + prices[i])
                dp[j][1] = max(dp[j][1], dp[j-1][0] - prices[i])
        return dp[k][0]


    def maxprofit_free_k(self,prices):
            dp_i_0 = 0
            dp_i_1 = float("-inf")
            for price in prices:
                temp = dp_i_0
                dp_i_0 = max(dp_i_0, dp_i_1 + price)
                dp_i_1 = max(dp_i_1, temp-price)
            return dp_i_0

k = 2
prices = [3,2,6,5,0,3]
print(Solution().maxProfit(k,prices))
