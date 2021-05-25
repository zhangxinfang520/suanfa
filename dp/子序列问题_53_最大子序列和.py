# -*- coding:utf-8 -*-
#@Time : 2021-05-25 19:40
#@Author: zxf_要努力
#@File : 53_最大子序列和.py
'''
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
输入：nums = [1]
输出：1
输入：nums = [0]
输出：0
输入：nums = [-100000]
输出：-100000

最大连续数组
dp[i] 要么与前面dp[i-1] 组成一起 要么自己单独成一组
max(dp[i],dp[i-1]+nums[i])
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp = [0] *(len(nums))
        #base case
        dp[0] = nums[0]
        for i in range(1,len(nums)):

            dp[i] = max(nums[i],dp[i-1]+nums[i])
        return max(dp)
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums))