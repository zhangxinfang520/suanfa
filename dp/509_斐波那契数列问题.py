# -*- coding:utf-8 -*-
# @Time : 2021-05-12 10:27
# @Author: zxf_要努力
# @File : 509_斐波那契数列问题.py
'''
斐波那契数，通常用 F(n) 表示，形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给你 n ，请计算 F(n) 。

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1
输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3
'''


class Solution:
    '''第一种方法 暴力递归'''
    # def fib(self, n: int) -> int:
    #     if n==0:
    #         return 0
    #     if n==1 or n==2:
    #         return 1
    #     return self.fib(n-1)+self.fib(n-2)
    #
    # '''第二种方法 带备忘录的递归'''
    # def fib(self, n: int) -> int:
    #     result = dict()
    #     for i in range(1,n+1):
    #         result[i] = 0
    #     def helper(n:int,demo:dict):
    #         if n==0:return 0
    #         if n==1 or n==2:return 1
    #         if demo[n] != 0:
    #             return demo[n]
    #         demo[n] = helper(n-1,demo)+helper(n-2,demo)
    #         return demo[n]
    #     return helper(n,result)
    '''第三种方法'''

    def fib(self, n: int):
        result = list()
        for i in range(n + 1):
            result.append(0)
        result[1] = result[2] = 1
        for i in range(3, n + 1):
            result[i] = result[i - 1] + result[i - 2]
        return result[n]


print(Solution().fib(5))


class Solution:
    '''第一种方法 暴力递归'''
    # def fib(self, n: int) -> int:
    #     if n==0:
    #         return 0
    #     if n==1 or n==2:
    #         return 1
    #     return self.fib(n-1)+self.fib(n-2)
    #
    '''第二种方法 带备忘录的递归'''

    def fib(self, n: int):
        result = list()
        for i in range(n + 1):
            result.append(0)
        result[1] = result[2] = 1
        for i in range(3, n + 1):
            result[i] = result[i - 1] + result[i - 2]
        return result[n]
    '''第三种 空间复杂度 为1'''
    def fib1(self, n: int):
        pre,next = 1,1
        for i in range(3, n + 1):
            result = pre + next
            pre = next
            next = result
        return result

