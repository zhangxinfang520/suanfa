# -*- coding:utf-8 -*-
#@Time : 2021-06-17 22:19
#@Author: zxf_要努力
#@File : 51_N皇后.py
'''
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，
该方案中 'Q' 和 '.' 分别代表了皇后和空位。
'''
from typing import List
import copy

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        if n ==1:return [["Q"]]
        elif n==2 or n==3:return []
        else:
            ans = list()
            res = [["."]*n for _ in range(n)]

            def isValid(board, row, col):
                #检查正上方
                for i in range(row):
                    if board[i][col] == 'Q':
                        return False
                # 检查右斜上方
                i = row - 1
                j = col + 1
                while  i >= 0 and j < n:
                        if board[i][j] == 'Q':
                            return False
                        i -= 1
                        j += 1
                #检查左斜上方
                i = row - 1
                j = col - 1
                while i >= 0 and j >= 0:
                        if board[i][j] == 'Q':
                            return False
                        i -= 1
                        j -= 1
                return True

            def backtrace(row,res):
                if row == len(res):
                    temp = list()
                    for i in range(n):
                        temp.append("".join(res[i]))
                    ans.append(temp)
                else:
                    for col in range(n):
                        if not isValid(res,row,col):
                            continue
                        res[row][col] = 'Q'
                        backtrace(row+1,res)
                        res[row][col] = '.'

            backtrace(0,res)
            return ans


print(Solution().solveNQueens(4))

