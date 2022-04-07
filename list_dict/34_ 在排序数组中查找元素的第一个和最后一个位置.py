# -*- coding:utf-8 -*-
#@Time : 2021-07-31 21:12
#@Author: zxf_要努力
#@File : 34_ 在排序数组中查找元素的第一个和最后一个位置.py

'''
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
'''
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1,-1]
        n = len(nums)
        if target not in nums:
             return [-1,-1]
        index = nums.index(target)
        if index == n - 1:
            return [n-1,n-1]
        for i in range(index+1,n):
            if nums[i] != nums[index]:
                return [index,i-1]
        return [index,n-1]


nums = [2,2]
target = 2
print(Solution().searchRange(nums,target))