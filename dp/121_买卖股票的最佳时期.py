# -*- coding:utf-8 -*-
#@Time : 2021-05-31 21:57
#@Author: zxf_要努力
#@File : 121_买卖股票的最佳时期.py
'''
定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票
输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

'''
from typing import List


class Solution:
    #吃方法会超时
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        else:
            max_index = prices.index(max(prices))
            min_index = prices.index(min(prices))
            if max_index >= min_index:
                return max(prices)-min(prices)
            max_price = 0
            for i in range(0,len(prices)-1):
               j = i+1
               while j< len(prices):
                   if prices[i] < prices[j]:
                       max_price = max(max_price,prices[j]-prices[i])
                   j +=1

            return max_price
    #添加辅助变量
    #用一个变量记录一个历史最低价格 minprice，
    # 我们就可以假设自己的股票是在那天买的。那么我们在第 i 天卖出股票能得到的利润就是 prices[i] - minprice。

    def maxProfit1(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        else:
            max_index = prices.index(max(prices))
            min_index = prices.index(min(prices))
            if max_index >= min_index:
                return max(prices) - min(prices)
            inf = int(1e9)
            minprice = inf
            maxprofit = 0
            for price in prices:
                maxprofit = max(price-minprice,maxprofit)
                minprice = min(minprice,price)
            return maxprofit




list_num = [7,1,5,3,6,4]
print(Solution().maxProfit(list_num))




