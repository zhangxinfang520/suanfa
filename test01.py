# -*- coding:utf-8 -*-
#@Time : 2021-08-01 11:11
#@Author: zxf_要努力
#@File : test01.py
# class Solution1:
#     def TeamNums(self , height ):
#         # write code here
#         if len(height) < 3:
#             return 0
#         n = len(height)
#         res = 0
#         for i in range(2,n):
#             for j in range(0,i):
#                 x = j + 1
#                 while x < i:
#                     if (height[j] < height[x] and height[x] < height[i]) or (height[j] > height[x] and height[x] > height[i]):
#                         res +=1
#                     x += 1
#         return res


class Solution:
    def getMaximumResource(self , grid ):
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

    def single_other(self,grids):
        m, n = len(grids), len(grids[0])

        def dp(grid,i,j):
            if i < 0 or j < 0 or i == m or j == n:
                return 0
            if grid[i][j] == 0:
                return 0
            temp = grid[i][j]
            grid[i][j] = 0
            max_ = 0
            max_ = max(max_,dp(grid,i+1,j))
            max_ = max(max_,dp(grid,i,j+1))
            max_ = max(max_,dp(grid,i-1,j))
            max_ = max(max_,dp(grid,i,j-1))
            grid[i][j] = temp
            return max_ + temp
        res = 0
        for i in range(m):
            for j in range(n):
                if grids[i][j] !=0:
                    res = max(res,dp(grids,i,j))
        return res



if __name__ == '__main__':

    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    print(Solution().getMaximumResource(grid))

