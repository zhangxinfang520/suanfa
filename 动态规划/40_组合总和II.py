# -*- coding:utf-8 -*-
#@Time : 2021-07-20 14:32
#@Author: zxf_要努力
#@File : 40_组合总和II.py
'''
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次。
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
'''
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        track = []
        candidates.sort()
        
        def backtrack(start,track, target):
            if target == 0:
                temp = sorted(track)
                if temp not in result:
                    result.append(temp)
                return
            if start == n:
                return
            for i in range(start,n):
                if (target - candidates[i]) >= 0:
                    track.append(candidates[i])
                    target -= candidates[i]
                    backtrack(i+1,track,target)
                    target += candidates[i]
                    track.pop()
        backtrack(0,track,target)
        return result


candidates =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 27
print(Solution().combinationSum2(candidates,target))
                
                
                