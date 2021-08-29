# -*- coding:utf-8 -*-
#@Time : 2021/8/29 16:35
#@Author: zxf_要努力
#@File : 198_打家结舍.py
'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，
一夜之内能够偷窃到的最高金额。

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def dp(start):
            if start >=n:
                return 0
            res = 0
            res = max(res,dp(start+1),nums[start]+dp(start+2))
            return res
        return dp(0)

    def rob1(self,nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,n):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[n-1]

    def rob3(self,nums):
        n = len(nums)
        dp_i_1, dp_i_2 = 0, 0
        dp_i = 0
        for i in range(n-1,-1,-1):
            dp_i = max(dp_i_1,dp_i_2+nums[i])
            dp_i_2 = dp_i_1
            dp_i_1 = dp_i
        return dp_i

if __name__ == '__main__':
    nums = [2,1,1,2]
    print(Solution().rob1(nums))