# -*- coding:utf-8 -*-
#@Time : 2021-06-30 19:25
#@Author: zxf_要努力
#@File : 01.py
'''
给你一个有序数组 nums ，请你原地删除重复出现的元素，使每个元素 只出现一次 ，
返回删除后数组的新长度。
不要使用额外的数组空间，
你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成

'''
from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(cls,nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i] == nums[i-1]:
                for j in range(i,n-1):
                    nums[j] = nums[j+1]
                n -=1
        return n

nums = [1,2,3,4,5,6,6,6,6,6,6]

print(Solution.removeDuplicates(Solution(),nums))