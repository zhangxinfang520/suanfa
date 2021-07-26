# -*- coding:utf-8 -*-
#@Time : 2021-07-26 19:13
#@Author: zxf_要努力
#@File : 4_寻找两个正序数组的中位数.py
'''
给定两个大小分别为 m 和 n 的正序（从小到大）
数组 nums1 和 nums2。
请你找出并返回这两个正序数组的 中位数 。
输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

输入：nums1 = [], nums2 = [1]
输出：1.00000
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0 :
            return float(0)
        if len(nums1) == 0:
            return self.find_mid_form_one_lists(nums2)
        if len(nums2) == 0:
            return self.find_mid_form_one_lists(nums1)
        nums = self.megre_lists_2_list(nums1,nums2)

        return self.find_mid_form_one_lists(nums)

    def megre_lists_2_list(self,nums1,nums2):
        nums = []
        while nums1 and nums2:
            if nums1[0] <nums2[0]:
                temp = nums1.pop(0)
                nums.append(temp)
            else:
                temp = nums2.pop(0)
                nums.append(temp)
        if nums1:
            for x in nums1:
                nums.append(x)
        if nums2:
            for x in nums2:
                nums.append(x)
        return nums

    def find_mid_form_one_lists(self,nums):
        if len(nums) % 2 == 0:
            return float(nums[ len(nums) // 2 ] + nums[ len(nums) // 2 - 1]) / 2
        else:
            return float(nums[len(nums) // 2] )

nums = [1]
nums1 = [1,3,5]
nums2 = [2,4,6]

print(Solution().findMedianSortedArrays(nums1,nums2))