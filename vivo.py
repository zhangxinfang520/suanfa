# -*- coding:utf-8 -*-
#@Time : 2021/9/22 15:02
#@Author: zxf_要努力
#@File : vivo.py

class Solution:
    def maxRollingHeroes(self,heroes):
        if len(heroes) == 1:
            return 1
        n,k = len(heroes),len(heroes[0])
        heroes = sorted(heroes,key= lambda x: (x[0],[-x[i] for i in range(1,k)]))
        dp = [1] * n
        for i in range(1,n):
            for j in range(0,i):
                if self.is_Valid(heroes,i,j,k):
                    dp[i] = max(dp[i],dp[j]+1)
        if max(dp) == 1:
            return 0
        return max(dp)

    def is_Valid(self,heroes,i,j,k):
        for x in range(0,k):
            if heroes[i][x] <= heroes[j][x]:
                return False
        return True


        
if __name__ == '__main__':
    heroes = [[60,35,20],[30,40,30],[40,50,40],[50,60,50]]
    print(Solution().maxRollingHeroes(heroes))