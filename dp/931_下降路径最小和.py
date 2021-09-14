# -*- coding:utf-8 -*-
#@Time : 2021-05-16 20:46
#@Author: zxf_要努力
#@File : 931_下降路径最小和.py
'''
给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和
下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。
在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。
具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col)
或者 (row + 1, col + 1)

输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
输出：13
解释：下面是两条和最小的下降路径，用加粗标注：
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]

输入：matrix = [[-19,57],[-40,-5]]
输出：-59
解释：下面是一条和最小的下降路径，用加粗标注：
[[-19,57],
 [-40,-5]]

'''
from typing import List

from joblib.numpy_pickle_utils import xrange


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
         m = len(matrix)
         n = len(matrix[0])

         memo = [[-1]*n for _ in range(m)]

         def dp(grid,i,j):

             # 如果索引越界 返回一个很大的值
             if i>=m or j>=n or j< 0:
                 return float('inf')
             # base case
             if i == (m-1):
                return grid[i][j]

             if memo[i][j] !=-1:
                 return memo[i][j]
             #状态方程
             memo[i][j] = min(dp(grid,i+1,j-1),dp(grid,i+1,j),dp(grid,i+1,j+1)) + grid[i][j]
             return memo[i][j]

         return min(dp(matrix,0,i) for i in range(n))

    def minFallingPathSum2(self, A):
        '''答案思路 '''
        while len(A) >= 2:
            row = A.pop()
            #想不到得到一个生成器对象
            for i in xrange(len(row)):
                A[-1][i] += min(row[max(0, i - 1): min(len(row), i + 2)])
        return min(A[0])



matrix = [[-48]]
print(Solution().minFallingPathSum(matrix))