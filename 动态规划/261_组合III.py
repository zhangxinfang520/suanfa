# -*- coding:utf-8 -*-
#@Time : 2021/9/3 20:51
#@Author: zxf_要努力
#@File : 261_组合III.py
'''
找出所有相加之和为 n 的 k 个数的组合。
组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

所有数字都是正整数。
解集不能包含重复的组合。
'''
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        nums = [i for i in range(1,11)]
        def backtrack(track,index,target):
            if len(track) == k and target == 0:
                res.append(track[:])
                return
            if len(track) == k or index== len(nums):
                return
            for i in range(index,len(nums)):
                if target- nums[i] >= 0 :
                    track.append(nums[i])
                    backtrack(track,index+1,target-nums[i])
                    track.pop()
        backtrack([],0,n)
        return res

if __name__ == '__main__':
    k = 3
    n = 9
    print(Solution().combinationSum3(k, n))
