# -*- coding:utf-8 -*-
#@Time : 2021-06-07 22:29
#@Author: zxf_要努力
#@File : 714_买卖股票最佳时期.py
'''

给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

注意：这里的一笔交易指买入持有并卖出股票的整
输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
输出: 8
解释: 能够达到的最大利润:
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        for price in prices:
            temp = dp_i_0
            dp_i_0 = max(dp_i_0,dp_i_1+price)
            dp_i_1 = max(dp_i_1,temp - price-fee)
        return dp_i_0