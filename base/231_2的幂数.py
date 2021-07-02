# -*- coding:utf-8 -*-
#@Time : 2021-07-01 20:43
#@Author: zxf_要努力
#@File : 231_2的幂数.py
'''
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；
否则，返回 false 。
如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False
        flag = True
        while flag and n!=1:
            if n % 2 == 0:
                flag = True
            else:
                flag = False
            n = n / 2

        if not flag:
            return False
        if n==1:
            return True

    def other_method(self,n:int):
        '''
        一个数如果是 2 的指数，那么它的二进制表示一定只含有一个 1：
        :param n:
        :return:
        '''
        if n<=0:
            return False
        return (n &(n-1)) == 0;

n = 4
print(Solution().isPowerOfTwo(n))