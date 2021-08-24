# -*- coding:utf-8 -*-
#@Time : 2021/8/24 11:44
#@Author: zxf_要努力
#@File : 005_单词长度的最大乘积.py
'''
给定一个字符串数组 words，请计算当两个字符串 words[i] 和 words[j]
不包含相同字符时，它们长度的乘积的最大值。假设字符串中只包含英语的小写字母。
如果没有不包含相同字符的一对字符串，返回 0。

输入: words = ["abcw","baz","foo","bar","fxyz","abcdef"]
输出: 16
解释: 这两个单词为 "abcw", "fxyz"。它们不包含相同字符，且长度的乘积最大。

输入: words = ["a","ab","abc","d","cd","bcd","abcd"]
输出: 4
解释: 这两个单词为 "ab", "cd"。

输入: words = ["a","aa","aaa","aaaa"]
输出: 0
解释: 不存在这样的两个单词。
'''
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        dp = [ [0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                if i == j:
                    dp[i][j] = 0
                else:
                    if self.is_valid(words[i],words[j]):
                        dp[i][j] = len(words[i]) * len(words[j])
                    else:
                        dp[i][j] = 0
        res = 0
        for i in range(n):
            res = max(res,max(dp[i]))
        return res

    def is_valid(self,str_A, str_B):
        list_A = set(list(str_A))
        list_B = set(list(str_B))
        if list_A.intersection(list_B):
            return False
        return True


if __name__ == '__main__':
    words = ["abcw","baz","foo","bar","fxyz","abcdef"]
    print(Solution().maxProduct(words))