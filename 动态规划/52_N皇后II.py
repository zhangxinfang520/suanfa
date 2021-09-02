# -*- coding:utf-8 -*-
#@Time : 2021/9/1 16:32
#@Author: zxf_要努力
#@File : 52_N皇后II.py

class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 1:
            return [["Q"]]
        elif n == 2 or n == 3:
            return []
        else:
            ans = list()
            res = [["."] * n for _ in range(n)]

            def isValid(board, row, col):
                # 检查正上方
                for i in range(row):
                    if board[i][col] == 'Q':
                        return False
                # 检查右斜上方
                i = row - 1
                j = col + 1
                while i >= 0 and j < n:
                    if board[i][j] == 'Q':
                        return False
                    i -= 1
                    j += 1
                # 检查左斜上方
                i = row - 1
                j = col - 1
                while i >= 0 and j >= 0:
                    if board[i][j] == 'Q':
                        return False
                    i -= 1
                    j -= 1
                return True

            def backtrace(row, res):
                if row == len(res):
                    temp = list()
                    for i in range(n):
                        temp.append("".join(res[i]))
                    ans.append(temp)
                else:
                    for col in range(n):
                        if not isValid(res, row, col):
                            continue
                        res[row][col] = 'Q'
                        backtrace(row + 1, res)
                        res[row][col] = '.'

            backtrace(0, res)
            return ans

    def is_valid(self, board, row, col, n):
        # 检查上方
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # 检查右斜上方
        i = row - 1
        j = col + 1
        while i > 0 and j < n:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        # 检查 左斜上方
        i = row - 1
        j = col - 1
        while i < 0 and j < 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        return True

if __name__ == '__main__':
    print(Solution().totalNQueens(9))



