# -*- coding:utf-8 -*-
#@Time : 2021-07-15 13:47
#@Author: zxf_要努力
#@File : 13.py
'''
最长公共前缀
如果不存在公共前缀，返回空字符串 ""。
输入：strs = ["flower","flow","flight"]
输出："fl"
输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
'''
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        str = strs[0]
        for i in range(1,len(strs)):
            str = self.get_same_prex(str,strs[i])
            if str == "":
                return ""
        return str
            
    def get_same_prex(self,str1,str2):
        res = ""
        i,j = 0,0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                res += str1[i]
                i +=1
                j +=1
            else:
                break
        return res


strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))
        
        
        
            
            