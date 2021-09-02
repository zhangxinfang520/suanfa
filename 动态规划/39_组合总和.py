# -*- coding:utf-8 -*-
#@Time : 2021-07-20 13:56
#@Author: zxf_要努力
#@File : 39_组合总和.py
'''
给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。
candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 
输入: candidates = [2,3,6,7], target = 7
输出: [[7],[2,2,3]]
输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]

'''
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        track = []
        n = len(candidates)

        def backtrack(target,track,idx):
            if target == 0:
                result.append(track[:])
                return
            if idx == n:
                return
            backtrack( target, track, idx + 1)
            if (target - candidates[idx]) >= 0:
                track.append(candidates[idx])
                backtrack(target-candidates[idx],track,idx)
                track.pop()
        backtrack(target,track,0)
        return result





candidates = [2,3,6,1,2,5,7]
target = 7

print(Solution().combinationSum(candidates,target))