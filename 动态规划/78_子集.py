# -*- coding:utf-8 -*-
#@Time : 2021-06-21 22:33
#@Author: zxf_要努力
#@File : 78_子集.py
'''
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
输入：nums = [0]
输出：[[],[0]]

解题思路：
    知道了规模更小的子问题的结果，
    具体来说就是，现在让你求 [1,2,3] 的子集，如果你知道了 [1,2] 的子集，是否可以推导出 [1,2,3] 的子集呢？先把  [1,2] 的子集写出来瞅瞅：
   [ [],[1],[2],[1,2] ]
规律：
subset([1,2,3]) - subset([1,2])
= [3],[1,3],[2,3],[1,2,3]
而这个结果，就是把 sebset([1,2]) 的结果中每个集合再添加上 3。

subset([1,2,3])
= A + [A[i].add(3) for i = 1..len(A)]
'''
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 : return [[]]
        res = list()
        self.backtrack(nums,0,[],res)
        return res

    def backtrack(self,nums,start,path,res):
        res.append(path[:])
        for i in range(start,len(nums)):
            path.append(nums[i])
            # 因为 nums 不包含重复元素，并且每一个元素只能使用一次
            # 所以下一次搜索从 i + 1 开始
            self.backtrack(nums,i+1,path,res)
            path.pop()
nums = [1,2,3]
print(Solution().subsets(nums))
