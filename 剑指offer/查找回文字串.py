# -*- coding:utf-8 -*-
#@Time : 2021/9/11 20:01
#@Author: zxf_要努力
#@File : 查早回文字串.py

class Solution:
    def fuDuJi(self, s):
        # write code here
        return self.test02(s)

    def test02(self, s):
        s_ = ""
        temp, n = 0, len(s)
        if len(s) == 1:
            return s[0]
        for i in range(n):
            length, res = self.find_singe(s, i, i)
            if length > temp:
                s_ = res
                temp = length
            length, res = self.find_singe(s, i, i + 1)
            if length > temp:
                s_ = res
                temp = length
        return s_

    def find_singe(self, s, i, j):
        n = len(s)
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            i -= 1
            j += 1
            res += 1
        return res, s[i + 1:j]