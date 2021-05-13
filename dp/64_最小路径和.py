# -*- coding:utf-8 -*-
#@Time : 2021-05-13 16:39
#@Author: zxf_要努力
#@File : 64_最下路径和.py
'''
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
输入：grid = [[1,2,3],[4,5,6]]
输出：12
1->2->3->6
'''
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = [[-1]*n for _ in range(m) ]
        def dp(grid,i,j):
            if i==0 and j==0:
                return grid[0][0]
            #如果索引出界，返回一个很大的值，
            # 保证在取min的时候不会被取到
            if i<0 or j <0:
                return float('inf')
            if memo[i][j] !=-1:
                return memo[i][j]
            #左边和上面的最小路径和加上 grid[i][j]
            #就是达到（i，j）的最小路径和
            memo[i][j] = min(dp(grid ,i-1,j),dp(grid,i,j-1))+grid[i][j]
            return memo[i][j]
        return dp(grid,m-1,n-1)
grid = [[1,3,1],[1,5,1],[4,2,1]]

print(Solution().minPathSum(grid))
