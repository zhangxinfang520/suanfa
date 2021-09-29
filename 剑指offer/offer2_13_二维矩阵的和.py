# -*- coding:utf-8 -*-
#@Time : 2021/9/22 8:40
#@Author: zxf_要努力
#@File : offer2_13_二维矩阵的和.py
'''
给定一个二维矩阵 matrix，以下类型的多个请求：

计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
实现 NumMatrix 类：

NumMatrix(int[][] matrix) 给定整数矩阵 matrix 进行初始化
int sumRegion(int row1, int col1, int row2, int col2) 返回左上角 (row1, col1) 、右下角 (row2, col2) 的子矩阵的元素总和。

输入:
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
输出:
[null, 8, 11, 12]

解释:
NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)

假设 preSum[i][j] 表示 表示子矩阵（0,0）,（i，j）的和
则子矩阵（row1,col1）,(row2,col2)的和
= preSum[row2][col2] - preSum[row1-1][col2] - preSum[row2][col1-1] + preSum[row1-1][col1-1]

'''
from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])

        self.sum = [[0]*(n+1) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                self.sum[i][j+1] = self.sum[i][j] + matrix[i][j]


    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     if row1 < 0 or row2 >= self.row or row1 > row2:
    #         return 0
    #     if col1 < 0 or col1 >= self.col or col1 > col2:
    #         return 0
    #     self.memo = dict()
    #     sum = 0
    #     if (row1,row2,col1,col2) not in self.memo:
    #         for i in range(row1,row2+1):
    #             for j in range(col1,col2+1):
    #                 sum += self.matrix[i][j]
    #         self.memo[ (row1,row2,col1,col2)] = sum
    #         return sum
    #     else:
    #         return self.memo[(row1,row2,col1,col2)]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0
        for i in range(row1,row2+1):
            sum +=self.sum[i][col2+1] - self.sum[i][col1]
        return sum





numMatrix = NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]])

print(numMatrix.sumRegion(1,2,2,4))