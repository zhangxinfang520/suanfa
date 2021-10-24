# -*- coding:utf-8 -*-
#@Time : 2021/10/13 14:55
#@Author: zxf_要努力
#@File : 59_螺旋矩阵 II.py
'''
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，
且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

输入：n = 1
输出：[[1]]
'''
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        dir_list = [(0,1),(1,0),(0,-1),(-1,0)]
        col,row,index = 0,0,0
        matrix = [[0] * n for _ in range(n)]
        for i in range(n*n):
            matrix[row][col] = i + 1
            dx,dy = dir_list[index]
            r,c = row+dx,col+dy
            if r < 0 or r>=n or c < 0 or c >=n or matrix[r][c] > 0:
                index = (index + 1) % 4
                dx, dy = dir_list[index]
            row, col = row + dx, col + dy
        return matrix

if __name__ == '__main__':
    print(Solution().generateMatrix(4))


