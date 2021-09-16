# -*- coding:utf-8 -*-
#@Time : 2021/9/16 19:46
#@Author: zxf_要努力
#@File : 54_螺旋矩阵.py
'''
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
'''
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    a = zip(*matrix)
    print(a)
    print(list(zip(*matrix)))
    print(Solution().spiralOrder(matrix))