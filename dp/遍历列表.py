# -*- coding:utf-8 -*-
#@Time : 2021-08-07 16:55
#@Author: zxf_要努力
#@File : 遍历列表.py
'''
遍历一个gird 可以上下左右遍历

'''
class Solution:
    def getMaximumResource(self, grid):
        # write code here
        m , n = len(grid),len(grid[0])
        memo = [[-1] * n for _ in range(m)]
        memo1 = [[-1] * n for _ in range(m)]
        res = 0
        def dp(grids, i, j):
            # 如果索引越界 返回一个很大的值
            if i < 0 or j < 0 or i == m or j ==n:
                return float('-inf')
            if memo1[i][j] == 1:
                return float('-inf')
            if memo[i][j] != -1 and memo1[i][j] !=-1:
                return memo[i][j]
            if memo[i][j] != -1 and memo1[i][j] == 1:
                return float('-inf')
            if grids[i][j] == 0:
                return float('-inf')
            memo1[i][j] = 1
            memo[i][j] = max(0,dp(grids, i - 1, j), dp(grids, i, j - 1)) + grids[i][j] #上左
            memo[i][j] = max(memo[i][j],max(0,dp(grids, i - 1, j), dp(grids, i, j + 1)) + grids[i][j])#上右
            memo[i][j] = max(memo[i][j],max(0,dp(grids, i + 1, j), dp(grids, i, j - 1)) + grids[i][j] ) # 下左
            memo[i][j] = max(memo[i][j],max(0,dp(grids, i + 1, j), dp(grids, i, j + 1)) + grids[i][j] )  #下右
            return memo[i][j]
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] !=0:
                    res = max(res,dp(grid, i, j))
                    memo = [[-1] * n for _ in range(m)]
                    memo1 = [[-1] * n for _ in range(m)]
        return res


    def othermethod(self,grid):
        m, n = len(grid), len(grid[0])
        res = 0
        def dp(memo,i,j):
            if i < 0 or j < 0 or i == m or j == n:
                return 0
            if memo[i][j] == 0:
                return 0
            temp = memo[i][j]
            memo[i][j] = 0
            Max = 0
            Max = max(Max,dp(memo,i-1,j))
            Max = max(Max,dp(memo,i+1,j))
            Max = max(Max,dp(memo,i,j-1))
            Max = max(Max,dp(memo,i,j+1))
            memo[i][j] = temp
            return Max + temp
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    res = max(res,dp(grid, i,j))
        return res


if __name__ == '__main__':
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    print(Solution().othermethod(grid))