# -*- coding:utf-8 -*-
#@Time : 2021-06-06 23:14
#@Author: zxf_要努力
#@File : 309_最佳买卖股票时机含冷冻期.py
'''
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

解释：第 i 天选择 buy 的时候，要从 i-2 的状态转移，而不是 i-1 。
每次 sell 之后要等一天才能继续交易。只要把这个特点融入上一题的状态转移方程即可
'''
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp_i_0 = 0
        dp_i_1 = float("-inf")
        dp_pre_0 = 0  # 这个代表i-2
        for price in prices:
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, dp_pre_0 - price)
            dp_pre_0 = temp
        return dp_i_0


if __name__ == '__main__':
    nums = [1, 2, 3, 0, 2]
    print(Solution().maxProfit(nums))
