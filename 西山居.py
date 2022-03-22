# encoding: utf-8
"""
@author: zxf_要努力
@file: 西山居.py
@time: 2022/3/22 19:30
"""

import sys


def xor(result_list):
    result = 0
    for r in result_list:
        result ^= r
    return result


def get_all_path(result, k):
    n, m = len(result), len(result[0])
    res = []

    def dp(i, j, total):
        if i == n-1 and j == m-1:
            if xor(total) ^ result[i][j] == k:
                res.append(1)
            return
        if i >= n or j >= m:
            return
        total.append(result[i][j])
        dp(i + 1, j, total)
        dp(i, j + 1, total)
        total.pop()

    dp(0, 0, [])
    return len(res)


if __name__ == '__main__':
    # n, m, k = list(map(int, sys.stdin.readline().strip().split(" ")))
    # maxtri = [[0] * m for _ in range(n)]
    # for i in range(n):
    #     temp = list(map(int, sys.stdin.readline().strip().split(" ")))
    #     for j in range(m):
    #         maxtri[i][j] = temp[j]
    matrix = [[1,2,4],[2,4,9]]
    k = 15
    print(get_all_path(matrix, k))
