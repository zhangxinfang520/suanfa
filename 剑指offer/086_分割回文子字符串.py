# -*- coding:utf-8 -*-
#@Time : 2021/8/30 11:48
#@Author: zxf_要努力
#@File : 086_分割回文子字符串.py
'''
给定一个字符串 s ，请将 s 分割成一些子串，使每个子串都是 回文串 ，返回 s 所有可能的分割方案。
'''
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        for i in range(len(s)):
            re = self.get_dorm(s,i)
            res.append(re[:])
        return res

    def get_dorm(self,s,i):
        '''i代表 窗口的长度'''
        re = []
        n = len(s)
        for i in range(n):
            pass
if __name__ == '__main__':
    s = "googlelgoo"
    print(Solution().partition(s))