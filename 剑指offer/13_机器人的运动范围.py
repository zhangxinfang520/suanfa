# -*- coding:utf-8 -*-
#@Time : 2021-08-10 18:47
#@Author: zxf_要努力
#@File : 13_机器人的运动范围.py
'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，
因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

输入：m = 2, n = 3, k = 1
输出：3
输入：m = 3, n = 1, k = 0
输出：1
'''
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        if k == 0:
            return 1
        memo = [[-1]*n for _ in range(m)]
        def is_cango(i,j, k):
            i_list = list(map(int,list(str(i))))
            j_list = list(map(int,list(str(j))))
            total = sum(i_list) + sum(j_list)
            return True if total <= k else False

        def dp(i,j,k):
            if i < 0 or j < 0 or i == m or j==n:
                return 0
            if memo[i][j] !=-1:
                return 0
            if not is_cango(i,j,k):
                return 0
            memo[i][j] = 1
            Max = 1
            Max = Max + dp(i-1, j, k) +dp(i+1, j, k) +dp(i, j-1, k)+dp(i, j+1, k)
            return Max

            return MAX
        return dp(0,0,k)

print(Solution().movingCount(5, 6, 7))

