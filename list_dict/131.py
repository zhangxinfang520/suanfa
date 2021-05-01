# -*- coding:utf-8 -*-
#@Time : 2021-03-07 18:15
#@Author: zxf_要努力
#@File : 131.py
'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案
输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
class Solution:
    def partition(self, s: str):
        if not s:
            return []
        if len(s) == 1:
            return [[s]]

        m = len(s)
        result = []
        dp = [[0 for i in range(m)] for i in range(m)]  # dp数组在这里记载的是，[i,j]双闭区间能否构成回文串。（1）若能构成，则dp[i,j]则为回文串长度。（2）若不能，dp[i,j]则为0
        for j in range(0, m):
            for i in range(0, j+1):
                if s[i] == s[j]:
                    if j-i < 3 or dp[i+1][j-1] > 0:
                        dp[i][j] = j-i+1
                    else:
                        dp[i][j] = 0
                else:
                    dp[i][j] = 0
        def dfs_helper(i, temp):  # 深度优先遍历，对于当前的位置i，看一下[i,j]能否构成回文串，若能，则继续深度优先遍历，到达极限则记录结果。记得回溯
            nonlocal dp, result, s
            if i == len(dp):
                result.append(temp.copy())

            for j in range(i, len(dp)):
                if dp[i][j]:
                    temp.append(s[i:j+1])
                    dfs_helper(j+1, temp)
                    temp.pop()

        temp_result = []
        dfs_helper(0, temp_result)
        return result
a ="aab"
print(Solution().partition(a))