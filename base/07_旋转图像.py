# -*- coding:utf-8 -*-
#@Time : 2021-07-08 18:42
#@Author: zxf_要努力
#@File : 旋转图像.py
'''
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。
请不要 使用另一个矩阵来旋转图像。
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]

'''
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if n == 1:
            return matrix
        for layer in range(0,n // 2):
            first = layer
            last = n - 1 - layer
            for i in range(first,last):
                offset = i - first
                temp = matrix[first][i]
                #左侧一列移动到顶部
                matrix[first][i] = matrix[last-offset][first]
                #底部移动到左侧
                matrix[last-offset][first] = matrix[last][last-offset]
                #右侧移到底部
                matrix[last][last - offset] = matrix[i][last]
                #顶部移到右侧
                matrix[i][last] = temp
        return matrix

    def other_method(self,matrix):
        n = len(matrix)
        if n == 1:
            return matrix
        for i in range(n//2):
             tmp = matrix[i]
             matrix[i] = matrix[n-i-1]
             matrix[n-i-1] = tmp

        for i in range(0,n):
            for j in range(i+1,n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().other_method(matrix))



