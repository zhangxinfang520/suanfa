# -*- coding:utf-8 -*-
#@Time : 2021-03-08 21:19
#@Author: zxf_要努力
#@File : 1.py
'''
给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍
你可以按任意顺序返回答案
示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]

'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list = []
        for i in range(1,len(nums)):
            for j in range(0,i):
                if nums[j] ==nums[i]:
                    continue
                if nums[i] + nums[j] ==target:
                    list.append(i)
                    list.append(j)
        return list
a =[2,7,11,15]
print(Solution().twoSum(a,9))