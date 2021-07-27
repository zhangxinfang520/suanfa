# -*- coding:utf-8 -*-
#@Time : 2021-07-24 20:23
#@Author: zxf_要努力
#@File : 5_最长回文子串.py
'''
给你一个字符串 s，找到 s 中最长的回文子串。
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
输入：s = "cbbd"
输出："bb"

令dp[i][j]表示S[i]至S[j]所表示的子串是否是回文子串，是则为1，不是为0。这样根据S[i]是否等于S[j]，可以把转移情况分为两类：
         ①若S[i]=S[j],那么只要S[i+1]和S[j-1]是回文子串，S[i+1]至S[j-1]就是回文子串；
         如果S[i+1]至S[j-1]不是回文子串，则S[i]至S[j]一定不是回文子串。
         ②若S[i]!=S[j]，那S[i]至S[j]一定不是回文子串

边界dp[i][i]=1,dp[i][i+1]=(S[i]==S[i+1])?1:0 。
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        max_len = 1
        begin = 0
        #dp[i][j] 表示s【i到j】是够为回文子串
        dp = [[False] * n for _ in range(n)]
        #对角线为True
        for i in range(n):
            dp[i][i] = True
        #先枚举子串长度
        for L in range(2,n + 1):
            #枚举左边界
            for i in range(n):
             # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                #如果右边界越界 直接退出当前循环
                if j >= n:
                    break
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                        # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                        if dp[i][j] and j - i + 1 > max_len:
                            max_len = j - i + 1
                            begin = i
        return s[begin:begin + max_len]

    def longestPalindrome1(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i+1)
            res = res if  len(res) > len(s1) else s1
            res = res if  len(res) > len(s2) else s2
        return res

    def palindrome(self, s:str, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:l+1+r-l-1]


s = "a"
print(Solution().longestPalindrome1(s))