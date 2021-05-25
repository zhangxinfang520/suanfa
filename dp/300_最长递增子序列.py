# -*- coding:utf-8 -*-
#@Time : 2021-05-22 17:15
#@Author: zxf_要努力
#@File : 300_最长递增子序列.py
'''
给你一个整数数组 nums ，
找到其中最长严格递增子序列的长度。
子序列是由数组派生而来的序列，
删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
输入：nums = [0,1,0,3,2,3]
输出：4
输入：nums = [7,7,7,7,7,7,7]
输出：1

思路逐步递归
从第一个开始 判断 与前面的数值的大小
dp 数值 存放 以该值结尾的最大增长子序列
求该值的 最大增长子序列 寻找前面的小于该值的最长的子序列 加一
'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j]< nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)

        return max(dp)

nums = [10,9,2,5,3,7,101,18]
print(Solution().lengthOfLIS(nums))

