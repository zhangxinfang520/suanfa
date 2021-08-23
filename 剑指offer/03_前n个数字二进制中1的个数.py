# -*- coding:utf-8 -*-
#@Time : 2021/8/23 11:16
#@Author: zxf_要努力
#@File : 03_前n个数字二进制中1的个数.py
'''
给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，
并输出一个数组。
输入: n = 2
输出: [0,1,1]
解释:
0 --> 0
1 --> 1
2 --> 10
思路 ：如果过该数为奇数 则 一个的个数即为 前面一个偶数加一
如果为偶数 则其个数为和其除以2的个数一样的

'''
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        if n == 0:
            return [0]
        res = [0] *(n+1)
        for i in range(1,n+1):
            if (i&1) == 0:
                res[i] = res[i>>1]
            else:
                res[i] = res[i-1] + 1
        return res

if __name__ == '__main__':
    print(Solution().countBits(5))
