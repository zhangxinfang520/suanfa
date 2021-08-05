# -*- coding:utf-8 -*-
#@Time : 2021-08-05 10:42
#@Author: zxf_要努力
#@File : 647_回文子串.py
'''
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return  0
        total = 0
        for i in range(n):
            l = self.palindrome(s,i,i)
            r = self.palindrome(s,i,i+1)
            total += l
            total += r

        return total

    def palindrome(self,s,l,r):
        n = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -=1
            r +=1
            n +=1
        return n


s = "aaa"
print(Solution().countSubstrings(s))



