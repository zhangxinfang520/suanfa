# -*- coding:utf-8 -*-
#@Time : 2021-07-14 15:06
#@Author: zxf_要努力
#@File : 28_移动零.py
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow ,fast = 0,0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow +=1
            fast += 1
        for i in range(slow,fast):
            nums[i] = 0
        return nums
nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums))
    