# -*- coding:utf-8 -*-
#@Time : 2021-07-28 19:51
#@Author: zxf_要努力
#@File : 268_丢失的数字.py
'''
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。
8是丢失的数字，因为它没有出现在 nums 中。
输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。
1 是丢失的数字，因为它没有出现在 nums 中。
'''
from typing import List

class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


nums = [3,0,1]
print(Solution().missingNumber(nums))

