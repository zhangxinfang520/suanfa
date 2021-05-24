# -*- coding:utf-8 -*-
#@Time : 2021-05-24 19:54
#@Author: zxf_要努力
#@File : 背包问题_415_分割等和子集.py
'''
给你一个 只包含正整数 的 非空 数组 nums 。
请你判断是否可以将这个数组分割成两个子集，
使得两个子集的元素和相等。

示例 1：
输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11]

示例 2：
输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。\
该题技巧
首先对一个数组求和 如果 和为奇数 则 无法拆分成子集
如果是偶数 只需要 存在数组之和等于其和一半即可

'''
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        m = sum(nums)
        if m % 2 != 0:
            return False
        m //= 2
        dp = [[False]*(m+1) for _ in range(n+1)]
        for i in range(n + 1):
            dp[i][0] = True
        for i in range(1,n+1):
            for j in range(1,m+1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
        return dp[n][m]

nums = [2,5,3,2]
print(Solution().canPartition(nums))