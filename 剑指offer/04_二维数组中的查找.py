# -*- coding:utf-8 -*-
#@Time : 2021-08-09 10:46
#@Author: zxf_要努力
#@File : 04_二维数组中的查找.py
'''
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。
给定 target = 20，返回 false。
暴力解法
线性查找
    从二维数组的右上角开始查找。如果当前元素等于目标值，则返回 true。
    如果当前元素大于目标值，则移到左边一列。如果当前元素小于目标值，则移到下边一行。
    可以证明这种方法不会错过目标值。如果当前元素大于目标值，说明当前元素的下边的所有元素
    都一定大于目标值，因此往下查找不可能找到目标值，往左查找可能找到目标值。
    如果当前元素小于目标值，说明当前元素的左边的所有元素都一定小于目标值，
    因此往左查找不可能找到目标值，往下查找可能找到目标值。
        如果 num 和 target 相等，返回 true
        如果 num 大于 target，列下标减 1
        如果 num 小于 target，行下标加 1


'''
from typing import List


class Solution:
    def findNumberIn2DArray1(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == target:
                    return True
        return False

    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0:
            return False
        n, m = len(matrix), len(matrix[0])
        row, cols = 0, m-1
        while row < n and cols >= 0:
            if matrix[row][cols] == target:
                return True
            if matrix[row][cols] < target:
                row += 1
            elif  matrix[row][cols] > target:
                cols -=1
        return False

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

print(Solution().findNumberIn2DArray(matrix, 5))
print(Solution().findNumberIn2DArray(matrix, 20))