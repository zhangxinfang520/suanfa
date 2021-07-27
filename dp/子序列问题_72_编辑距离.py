# -*- coding:utf-8 -*-
#@Time : 2021-05-25 19:40
#@Author: zxf_要努力
#@File : 72_编辑距离.py
'''
给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符
输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

base case
word1 遍历完 word2还没有遍历完
word2 遍历完 word1 还没有遍历完

if j==-1 return i+1
if i==-1 return j+1

状态转移
if s1[i]=s2[j] 接着往前遍历
else
  min(
  插入，
  删除，
  替换
  )
插入 代表指针不往前移 总数加一
 dp(i, j - 1) + 1,
删除  和插入相反如果在str1插入也可以在str2删除效果一样   总数加一
 dp(i - 1, j) + 1,
替换 两个指针都往前移 总数加一
dp(i - 1, j - 1) + 1
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def dp(i,j):
            if i == -1: return j+1
            if j == -1: return i+1
            if word1[i] == word2[j]:
                return dp(i-1,j-1)
            else:
                return min(
                    dp(i-1,j)+1,
                    dp(i,j-1)+1,
                    dp(i-1,j-1)+1
                )
        return dp(len(word1)-1,len(word2)-1)


word1 = "horse"
word2 = "ros"
print(Solution().minDistance(word1, word2))



