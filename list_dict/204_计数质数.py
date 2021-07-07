# -*- coding:utf-8 -*-
#@Time : 2021-07-04 23:29
#@Author: zxf_要努力
#@File : 204_计数质数.py
'''
统计所有小于非负整数 n 的质数的数量。
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        sum = 0
        for i in range(2,n):
            if self.is_Primes(i):
                sum +=1
        return sum

    def is_Primes(self,n:int):
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i *= i
        return True


print(Solution().countPrimes(499979))


