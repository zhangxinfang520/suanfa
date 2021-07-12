# -*- coding:utf-8 -*-
#@Time : 2021-07-11 9:47
#@Author: zxf_要努力
#@File : 448_找到所有数组中消失的数据.py
'''
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，
并以数组的形式返回结果。
输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]
输入：nums = [1,1]
输出：[2]
'''


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        all_list = [i for i in range(1,n+1)]
        return list(set(all_list).difference(set(nums)))

nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(Solution().findDisappearedNumbers(nums))