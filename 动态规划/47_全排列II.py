# -*- coding:utf-8 -*-
#@Time : 2021-06-19 23:38
#@Author: zxf_要努力
#@File : 47_全排列II.py
'''
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

 输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = list()

        def all_sort(first=0):
            if first == n:
                temp = nums[:]
                if temp not in res:
                    res.append(nums[:])
            else:
                for i in range(first,n):
                    nums[first],nums[i] = nums[i], nums[first]
                    all_sort(first+1)
                    nums[first], nums[i] = nums[i], nums[first]
        all_sort()
        return res
nums = [1,1,2]
print(Solution().permuteUnique(nums))

