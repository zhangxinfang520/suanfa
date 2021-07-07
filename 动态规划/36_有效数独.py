# -*- coding:utf-8 -*-
#@Time : 2021-07-07 21:20
#@Author: zxf_要努力
#@File : 36_有效数独.py
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] == ".":
                    continue
                else:
                    temp = board[i][j]
                    board[i][j] = "."
                    if not self.isValid(board,i,j,temp):
                        return False
                    board[i][j] = temp

        return True

    def isValid(self, board, i, j, num, m=9):
        for x in range(0, m):
            if board[i][x] == num :
                return False
            if board[x][j] == num :
                return False
            z = (i // 3) * 3 + x // 3
            w = (j // 3) * 3 + x % 3
            if board[int(z)][int(w)] == num:
                return False
        return True

board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
print(Solution().isValidSudoku(board))