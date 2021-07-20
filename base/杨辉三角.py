# -*- coding:utf-8 -*-
#@Time : 2021-07-20 12:34
#@Author: zxf_要努力
#@File : 杨辉三角.py
'''
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
[1, 5, 10, 10, 5, 1]
[1, 6, 15, 20, 15, 6, 1]
[1, 7, 21, 35, 35, 21, 7, 1]
[1, 8, 28, 56, 70, 56, 28, 8, 1]
[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
'''

class Solution:
    def yanghui_angle(self):
        t = 0
        result = []
        for x in self.get_one_list():
            result.append(x)
            t +=1
            if t == 10:
                break
        return result

    def get_one_list(self):
        N = [1]
        while True:
            yield N
            S = N[:]
            S.append(0)
            N = [S[i - 1] + S[i] for i in range(0,len(S))]


print(Solution().yanghui_angle())