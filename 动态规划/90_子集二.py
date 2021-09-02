# -*- coding:utf-8 -*-
#@Time : 2021/9/2 15:17
#@Author: zxf_要努力
#@File : 90_子集二.py
'''
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列
输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
输入：nums = [0]
输出：[[],[0]]
'''
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
         n = len(nums)
         res = []
         nums.sort()

         def backtrack(index,track):

            res.append(track[:])
            for i in range(index,n):
                 if i > index and nums[i] == nums[i - 1]:
                     continue
                 track.append(nums[i])
                 backtrack(i+1,track)
                 track.pop()
         backtrack(0,[])
         return res 
    
if __name__ == '__main__':
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))
        