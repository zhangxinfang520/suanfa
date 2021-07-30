# -*- coding:utf-8 -*-
#@Time : 2021-07-29 9:50
#@Author: zxf_要努力
#@File : 50_pow(x,n).py
'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn）。
输入：x = 2.00000, n = 10
输出：1024.00000
输入：x = 2.10000, n = 3
输出：9.26100
输入：x = 2.00000, n = -2
输出：0.25000
解释：2-2 = 1/22 = 1/4 = 0.25
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.
        if n < 0:
            x = 1./ x
            n = -1 * n
        return self.qucikMul(x,n)

    def qucikMul(self,x,n):
        if n == 0:
            return 1.
        if n % 2 == 0:
            y = self.qucikMul(x,n//2)
            return  y * y
        else:
            y = self.qucikMul(x, n // 2)
            return y * y * x


print(Solution().myPow(2, 10))