# -*- coding:utf-8 -*-
#@Time : 2022/3/12 16:51
#@Author: zxf_要努力
#@File : 62_不同路径.py
'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？
'''

class Solution:
    nums = 0
    def unqiuePaths(self,m,n):
        def dp(x,y):
            if x == m-1 and y == n-1:
                self.nums +=1
            if x == m or y ==n:
                return
            dp(x+1,y)
            dp(x,y+1)
        dp(0,0)
        return self.nums
if __name__ == '__main__':
    solution = Solution()
    print(solution.unqiuePaths(3, 3))
