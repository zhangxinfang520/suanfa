# -*- coding:utf-8 -*-
#@Time : 2021-07-01 21:00
#@Author: zxf_要努力
#@File : 136_只出现一次的数字.py
'''给定一个非空整数数组，除了某个元素只出现一次以外，
其余每个元素均出现两次。找出那个只出现了一次的元素。
输入: [2,2,1]
输出: 1
输入: [4,1,2,1,2]
输出: 4
'''
from typing import List
'''一个数和它本身做异或运算结果为 0，
即 a ^ a = 0；
一个数和 0 做异或运算的结果为它本身，即 a ^ 0 = a'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        flag = True
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        for i in range(1,len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]

    def other_nums(self,nums):
        res = 0
        for num in nums:
            res ^= num
        return res

nums = [4,1,2,1,2]
print(Solution().singleNumber(nums))
print(Solution().other_nums(nums))

