# -*- coding:utf-8 -*-
#@Time : 2021-07-06 21:01
#@Author: zxf_要努力
#@File : 06.py
'''给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <2:
            return
        n = len(nums) - 1
        while nums[n] == 0 and n <= 0:
            n -=1
        if n < 0:
            return nums
        for i in range(n,-1,-1):
            if nums[i] == 0:
                for j in range(i,n):
                    nums[j] = nums[j+1]
                nums[n] = 0
                n -=1
        return nums


nums = [1,0,0,1]
print(Solution().moveZeroes(nums))