# -*- coding:utf-8 -*-
#@Time : 2021/10/13 10:15
#@Author: zxf_要努力
#@File : xunlei.py

class Solution:
    def get_matrix(self,n):
        if n == 1:
            return [1]
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        matrix = [[0] * n for _ in range(n)]
        row,col,index = 0,0,0
        for i in range(n*n):
            matrix[row][col] = i + 1
            x,y = dirs[index]
            r,c = row + x , col + y
            if r < 0 or r>=n or c < 0 or c >=n or matrix[r][c] > 0:
                index = (index+1) % 4 #顺时针旋转至下一个方向
                x,y = dirs[index]
            row,col = row + x, col+ y

        return matrix

if __name__ == '__main__':
    print(Solution().get_matrix(3))

