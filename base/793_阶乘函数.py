# -*- coding:utf-8 -*-
#@Time : 2021-07-03 22:48
#@Author: zxf_要努力
#@File : 793_阶乘函数.py
'''
输入一个非负整数 K，请你计算有多少个 n，满足 n! 的结果末尾恰好有 K 个 0。
'''

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        re = 0
        for i in range(0,float('inf')):
            if self.get_end_zero(i) < k:
                continue
            if self.get_end_zero(i) > k:
                break
            else:
                re +=1

    def get_end_zero(self,num:int)->int:
        res = 0
        division = 5
        while division <= num:
            res += num // division
            division *= 5

        return res

    def othermethod(self, K: int) -> int:
        a = lambda x: 0 if not x else a(x//5)+x//5
        l, r = K, K*7+1
        while l<r:
            mid = (l+r)//2
            p = a(mid)
            if p == K:
                return 5
            elif p < K:
                l = mid+1
            else:
                r = mid-1
        return 0


print(Solution().preimageSizeFZF(2))