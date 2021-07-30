# -*- coding:utf-8 -*-
#@Time : 2021-07-30 15:05
#@Author: zxf_要努力
#@File : 3__和为s的连续正数序列.py
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        res = list()
        for i in range(1,target+1):
            res.append(i)
        n = len(res)
        rk,ans = -1 , 0
        result = []
        occ = list()
        for i in range(n):
            if i!=0:
                occ.remove(res[i-1])
            while rk+1 <n and sum(occ) < target:
                occ.append(res[rk+1])
                rk +=1
            if sum(occ) == target and len(occ) > 1:
                result.append(occ[:])
        return result


print(Solution().findContinuousSequence(15))
