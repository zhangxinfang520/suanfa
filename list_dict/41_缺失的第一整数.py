# -*- coding:utf-8 -*-
#@Time : 2021-07-28 18:08
#@Author: zxf_要努力
#@File : 41_缺失的第一正数.py
'''
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
输入：nums = [1,2,0]
输出：3

输入：nums = [3,4,-1,1]
输出：2
输入：nums = [7,8,9,11,12]
输出：1
'''
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dict_list = []
        for i in range(len(nums)):
            if nums[i] > 0:
                dict_list.append(nums[i])

        if len(dict_list) == 0:
            return 1
        dict_list = list(set(dict_list))
        dict_list.sort()
        if dict_list[0] == 1:
            if len(dict_list) == (dict_list[-1] - dict_list[0] + 1):
                    return dict_list[-1] + 1
            else:
                for i in range(0,len(dict_list)-1):
                    if dict_list[i+1] - dict_list[i] > 1:
                        return dict_list[i] + 1
        else:
            return 1

    def othermethod(self,nums):
        n = len(nums)
        if 1 not in nums:
            return 1
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        for i in range(n):
            a = abs(nums[i])-1
            nums[a] = - abs(nums[a])
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1


nums =  [1,-1,0,5,-2,-3,5,7,8,9,11,12]
print(Solution().othermethod(nums))
