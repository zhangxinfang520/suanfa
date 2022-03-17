# encoding: utf-8
"""
@author: zxf_要努力
@file: 1763_最长的美好子字符串.py
@time: 2022/3/17 16:19
"""
'''
当一个字符串 s 包含的每一种字母的大写和小写形式 同时 出现在 s 中，就称这个字符串 s 是 美好 字符串。比方说，"abABB" 是美好字符串，因为 'A' 和 'a' 
同时出现了，且 'B' 和 'b' 也同时出现了。然而，"abA" 不是美好字符串因为 'b' 出现了，而 'B' 没有出现。
给你一个字符串 s ，请你返回 s 最长的 美好子字符串 。如果有多个答案，请你返回 最早 出现的一个。如果不存在美好子字符串，请你返回一个空字符串。
输入：s = "YazaAay"
输出："aAa"
解释："aAa" 是一个美好字符串，因为这个子串中仅含一种字母，其小写形式 'a' 和大写形式 'A' 也同时出现了。
"aAa" 是最长的美好子字符串。
输入：s = "Bb"
输出："Bb"
解释："Bb" 是美好字符串，因为 'B' 和 'b' 都出现了。整个字符串也是原字符串的子字符串。
输入：s = "c"
输出：""
解释：没有美好子字符串。
'''

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if not s :return ""
        for i,c in enumerate(s):
            ch = c.upper() if s.islower() else c.lower()
            if ch in s: continue
            left = self.longestNiceSubstring(s[0:i])
            right = self.longestNiceSubstring(s[i+1:])
            return left if len(left) >= len(right) else right
        return s
