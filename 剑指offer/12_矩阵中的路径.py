# -*- coding:utf-8 -*-
#@Time : 2021-08-13 9:41
#@Author: zxf_要努力
#@File : 12_矩阵中的路径.py
'''
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。
如果 word 存在于网格中，返回 true ；否则，返回 false 。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false
'''
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        #要遍历每一个从每一个字母出发是否都可以
        res = False
        for i in range(n):
            for j in range(m):
                res = res or self.is_valid(board, n, m,i,j,word)
                if res :
                     return True
        return res

    def is_valid(self, board, n, m, i_, j_, word):

        def backtarck(i,j,track):
            if track == word:
                return True
            len_track = len(track)
            len_word = len(word)
            if len_track > len_word:
                return False
            if  track != word[0:len_track]:
                return False

            if i<0 or j < 0 or i>=n or j >=m:
                return False
            if board[i][j] =="":
                return False

            temp = board[i][j]
            if temp not in word :
                return False
            board[i][j] = ""
            res = False
            res = res or backtarck(i+1,j,track+temp)
            res = res or backtarck(i-1,j,track+temp)
            res = res or backtarck(i,j+1,track+temp)
            res = res or backtarck(i,j-1,track+temp)
            board[i][j] = temp
            return res

        return backtarck(i_,j_,"")

    def is_valid1(self, board, n, m, i_, j_, word):

        memo = [[-1] * m for _ in range(n)]

        def backtarck(i,j,track):
            if track == word:
                return True
            if i<0 or j < 0 or i>=n or j >=m:
                return False
            if board[i][j] == "":
                return False
            temp = board[i][j]
            if temp not in word:
                return False
            board[i][j] = ""
            res = False
            res = res or backtarck(i+1,j,track+temp)
            res = res or backtarck(i-1,j,track+temp)
            res = res or backtarck(i,j+1,track+temp)
            res = res or backtarck(i,j-1,track+temp)
            board[i][j] = temp
            return res

        return backtarck(i_,j_,"")


if __name__ == '__main__':
    board = [["b","a","a","b","a","b"],["a","b","a","a","a","a"],["a","b","a","a","a","b"],["a","b","a","b","b","a"],["a","a","b","b","a","b"],["a","a","b","b","b","a"],["a","a","b","a","a","b"]]
    word = "aab"
    print(Solution().exist(board,word))




