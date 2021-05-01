# -*- coding:utf-8 -*-
#@Time : 2021-03-06 19:14
#@Author: zxf_要努力
#@File : 503.py
"""
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），
输出每个元素的下一个更大元素。
数字 x 的下一个更大的元素是按数组遍历顺序，这个数字之后的第一个比它更大的数，
这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 -1。

输入: [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
    数字 2 找不到下一个更大的数；
    第二个 1 的下一个最大的数需要循环搜索，结果也是 2。
"""
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        max_index = nums.index(max(nums))
        result = [0]*len(nums)
        for i in range(len(nums)):
            if  nums[max_index] == nums[i]:
                result[i] = -1
            else:
                if i < len(nums):
                    bool_change = False
                    for j in range(i+1,len(nums)):
                        if nums[j] > nums[i]:
                            bool_change = True
                            result[i] = nums[j]
                            break
                    if not bool_change:
                        for j in range(0,i):
                            if nums[j] > nums[i]:
                                result[i] = nums[j]
                                break
                else:
                    for j in range(0,len(nums)-1):
                        if nums[j] > nums[i]:
                            result[i] = nums[j]
                            break
        return result


a = [1,2,3,4,3]
s = Solution()
print(s.nextGreaterElements(a))