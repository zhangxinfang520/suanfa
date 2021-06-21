# -*- coding:utf-8 -*-
#@Time : 2021-06-16 23:06
#@Author: zxf_要努力
#@File : 46.py
'''
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列
。你可以 按任意顺序 返回答案。
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

输入：nums = [0,1]
输出：[[0,1],[1,0]]

输入：nums = [1]
输出：[[1]]
'''
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res =list()
        n = len(nums)
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            for i in range(first,n):
                #动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                #继续填充下一个数
                backtrack(first+1)
                #撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return res

nums = [1,2,3,5]
Solution().permute(nums)