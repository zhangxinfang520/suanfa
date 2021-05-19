# -*- coding:utf-8 -*-
#@Time : 2021-05-18 16:49
#@Author: zxf_要努力
#@File : 516_最长回文子序列.py
'''
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。
可以假设 s 的最大长度为 1000 。
输入 输出
"bbbab" 4 一个可能的最长回文子序列为 "bbbb"。
"cbbd" 2 一个可能的最长回文子序列为 "bb"。
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        str1 = list(s)
        str2 = str1[::-1]
        def dp(i,j):
            if i==-1 or j==-1:
                return 0
            if str1[i] == str2[j]:
                return 1+dp(i-1,j-1)
            else:
                return max(dp(i-1,j),dp(i,j-1))
        return dp(len(str1)-1,len(str1)-1)

text1 = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
print(Solution().longestPalindromeSubseq(text1))