# -*- coding:utf-8 -*-
#@Time : 2021-06-30 21:10
#@Author: zxf_要努力
#@File : 191_位一的个数.py
#编写一个函数，输入是一个无符号整数（以二进制串的形式），
# 返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

#利用位运算法 &
# n = n & (n-1) 只要n不等于0 每做一次位运算 1的数量 就会减少一个

class Solution:
    def hammingWeight(self, n: int) -> int:
        cout = 0
        while  n !=0:
            n = n & (n-1)
            cout +=1
        return cout
# a = 1011
# print(Solution().hammingWeight(a))

