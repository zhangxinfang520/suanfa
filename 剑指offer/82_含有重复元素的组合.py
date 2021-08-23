# -*- coding:utf-8 -*-
#@Time : 2021/8/23 12:30
#@Author: zxf_要努力
#@File : 82_含有重复元素的组合.py
'''
给定一个可能有重复数字的整数数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次，解集不能包含重复的组合。

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
        candidates.sort()
        res = []
        n = len(candidates)

        def backtrack(track,target,idx):
            if target == 0:
                # if track not in res:
                #     res.append(track[:])
                res.append(track[:])
                return
            if idx == n:
                return
            for i in range(idx,n):
                if i>idx and candidates[i]==candidates[i-1]:
                    continue
                if target - candidates[i] >= 0:
                    track.append(candidates[i])
                    backtrack(track,target-candidates[i],i+1)
                    track.pop()
        backtrack([],target,0)
        return res

if __name__ == '__main__':
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution().combinationSum2(candidates, target))