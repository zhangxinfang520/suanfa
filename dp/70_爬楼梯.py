# -*- coding:utf-8 -*-
#@Time : 2021-08-04 10:03
#@Author: zxf_要努力
#@File : 70_爬楼梯.py
'''

假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 0 :
            return 0
        memo = [0] * (n+1)
        memo[1] = 1
        memo[2] = 2
        for i in range(3,n+1):
            memo[i] = memo[i-2] + memo[i-1]
        return memo[n]

    def climbStairs1(self, n: int) -> int:
        if n < 0 :
            return 0
        res = []

        def backtrack(i):
            if i == 0:
                res.append(1)
            if i < 0:
                return False
            backtrack(i-1)
            backtrack(i-2)
        backtrack(n)
        return sum(res)

print(Solution().climbStairs(10))

