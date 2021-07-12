# -*- coding:utf-8 -*-
#@Time : 2021-07-12 14:55
#@Author: zxf_要努力
#@File : 10.py
'''
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

'''
import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict_s = {}
        dict_t = {}
        if len(s) != len(t):
            return False
        for str_s,str_t in zip(s,t):
            if str_s not in dict_s.keys():
                dict_s[str_s] = 1
            else:
                temp = dict_s[str_s]
                temp += 1
                dict_s[str_s] = temp
            if str_t not in dict_t.keys():
                dict_t[str_t] = 1
            else:
                temp = dict_t[str_t]
                temp += 1
                dict_t[str_t] = temp
        for key,value in dict_s.items():
            if key not in dict_t.keys():
                return False
            count = dict_t[key]
            if count != value:
                return False
        return True

    def other_method(self,s,t):

        return collections.Counter(s) == collections.Counter(t)

print(Solution().isAnagram("srrt", "rrst"))