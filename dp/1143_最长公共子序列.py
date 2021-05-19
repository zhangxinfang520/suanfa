# -*- coding:utf-8 -*-
#@Time : 2021-05-18 16:52
#@Author: zxf_要努力
#@File : 1143_最长公共子序列.py
'''
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。
如果不存在 公共子序列 ，返回 0 。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符
（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

输入：text1 = "abcde", text2 = "ace"
输出：3
解释：最长公共子序列是 "ace" ，它的长度为 3 。
输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。
输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。

"abcde" "afe" 2
'''
'''
这个子序列 只考虑位置 不一定一样
思路 从后往后往前遍历
            base case i==-1 or j==-1:
                return 0
            if str1[i] == str2[j]:
                return 1 + dp(i-1,j-1)
            else:
                return max(dp(i-1,j),dp(i,j-1))
            具有灵魂的一步
'''


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n = len(text1),len(text2)
        #构建dp table
        dp = [[0] *(n+1) for _ in range(m+1)]
        str1,str2= list(text1),list(text2)
        #进行转移
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]

    def longdp(self,text1: str, text2: str):
        str1,str2 = list(text1),list(text2)

        def dp(i,j):
            if i==-1 or j==-1:
                return 0
            if str1[i] == str2[j]:
                return 1 + dp(i-1,j-1)
            else:
                return max(dp(i-1,j),dp(i,j-1))

        return dp(len(str1)-1,len(str2)-1)

    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        '''这种方法 求的不是最长 求得是最优先的'''
        test1_list = list(text1)
        test2_list = list(text2)

        flag = True if len(test1_list) >= len(test2_list) else False
        test_dict = dict()
        if flag:
            list_dict = test1_list
        else:
            list_dict = test2_list
        for i,str in enumerate(list_dict):
            if str not in test_dict.keys():
                 test_dict[str] = [i]
            else:
                temp = test_dict[str]
                temp.append(i)
                test_dict[str] = temp
        count = 0
        loc = -1
        if flag:
            res_list = test2_list
        else:
            res_list = test1_list

        for i,str in enumerate(res_list):
            if str in test_dict.keys():
                index_list = test_dict[str]
                if index_list[-1] < loc:
                    continue
                for index in index_list:
                    if index > loc:
                        loc = index
                        count +=1
                        break
        return count



text1 = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"

text2 = "dbbc"
print(Solution().longestCommonSubsequence(text1, text2))