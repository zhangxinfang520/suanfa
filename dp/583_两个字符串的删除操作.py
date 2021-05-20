# -*- coding:utf-8 -*-
#@Time : 2021-05-19 21:27
#@Author: zxf_要努力
#@File : 583_两个字符串的删除操作.py
'''
给定两个单词 word1 和 word2，
找到使得 word1 和 word2
相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。
输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
'''

class Solution:
    #带备忘录 永远的神
    def minDistance(self,word1: str, word2: str)->int:
        str1_list = list(word1)
        str2_list = list(word2)
        n = len(str1_list)
        m = len(str2_list)

        memo = [[0] *(m-1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1_list[i-1] == str2_list[j-1]:
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i][j-1],memo[i-1][j])
        count = memo[-1][-1]
        return m+n-2*count

    #超时
    def minDistance1(self, word1: str, word2: str) -> int:
        str1_list = list(word1)
        str2_list = list(word2)
        if len(str1_list) ==0 or len(str2_list) == 0:
            return
        def dp(i,j):
            if i==-1 or j==-1:
                return 0
            if str1_list[i] == str2_list[j]:
                return 1+dp(i-1,j-1)
            else:
                return max(dp(i,j-1),dp(i-1,j))
        count = dp(len(str1_list)-1,len(str2_list)-1)
        return len(str1_list)+len(str2_list)-2*count

str1 = "dinitrophenylhydrazine"
str2 = "benzalphenylhydrazone"
print(Solution().minDistance(str1, str2))