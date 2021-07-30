# -*- coding:utf-8 -*-
#@Time : 2021-07-29 12:55
#@Author: zxf_要努力
#@File : 两举证相乘.py
import numpy as np

def two_mat_mul(mat1,mat2):
    row1, col1 = len(mat1), len(mat1[0])
    row2, col2 = len(mat2), len(mat2[0])
    assert  col1 == row2
    result = [[0] * col2 for _ in range(row1)]
    for i in range(row1):
        for x in range(col2):
            sum_one_row = 0
            for j in range(col1):
                sum_one_row += mat1[i][j] *mat2[j][x]
            result[i][x] = sum_one_row
    return result


mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mat2 = [[3, 1, 3], [2, 1, 4], [1, 1, 4]]
print(two_mat_mul(mat1,mat2))
print(np.dot(mat1,mat2))