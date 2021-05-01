# -*- coding:utf-8 -*-
#@Time : 2021-03-13 21:34
#@Author: zxf_要努力
#@File : 18.py
'''
四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组

示例 1：

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：
输入：nums = [], target = 0
输出：[]
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        i0,itarget=0,0
        for i,x in enumerate(nums):
            if x <= 0:
                i0 = i
            elif x>=target:
                itarget =i
                break
        return i0,itarget



nums = [1,0,-1,0,-2,2]
target = 0
a = Solution()
a.fourSum(nums,target)
