# -*- coding:utf-8 -*-
#@Time : 2021-07-30 15:18
#@Author: zxf_要努力
#@File : 3_连续子数组的最大和.py
'''
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大
输入: nums = [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        #这个递归不行 因为本地要从下往上递归
        #上界无法确定
        def dp(i):
            if i == n:
                return
            if i == 0:
                return nums[0]
            return max(nums[i],dp[i-1]+nums[i])
        return dp(1)

    def maxSubArray1(self,nums):
        n = len(nums)
        if n == 0:
            return 0
        #dp[i] 代表以nums[i] 结尾的和最大的连续子数组的和
        dp = [0] * n
        dp[0],res = nums[0],nums[0]
        for i in range(1,n):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            res = max(dp[i],res)
        return res
            

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray1(nums))