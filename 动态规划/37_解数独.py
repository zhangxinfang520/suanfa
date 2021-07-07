# -*- coding:utf-8 -*-
#@Time : 2021-06-28 20:47
#@Author: zxf_要努力
#@File : 37_解数独.py
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if self.backtrack(board,0,0):
            return board

    def backtrack(self,board,i,j,m=9,n=9):
        if j == n:#代表这一列已经穷举完了
            return self.backtrack(board,i+1,0)
        if i == m:
            return True
        if board[i][j] != ".":#如果有数字 不用穷举的
            return self.backtrack(board,i,j+1)
        #穷举
        for num in range(1,10):
            if not self.isValid(board,i,j,str(num)):
                continue
            board[i][j] = str(num)
            if self.backtrack(board,i,j+1):
                return True
            board[i][j] = "."

        return False

    def isValid(self,board,i,j,nums,n=9,m=9):
        for x in range(m):
            if board[i][x] == nums :
                return False
            if board[x][j] == nums :
                return False
            #判断3*3的网格
            z = (i//3) * 3 + x // 3
            w = (j//3) * 3 + x % 3
            if board[int(z)][int(w)] == nums:
                return False
        return True
# board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
#
# print(Solution().solveSudoku(board))


