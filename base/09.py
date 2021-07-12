# -*- coding:utf-8 -*-
#@Time : 2021-07-11 8:54
#@Author: zxf_要努力
#@File : 09.py
import collections
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        key_str_value_count = collections.OrderedDict()
        for i in range(len(s)):
            if s[i] in key_str_value_count.keys():
                temp = key_str_value_count[s[i]]
                temp +=1
                key_str_value_count[s[i]] = temp
            else:
                key_str_value_count[s[i]] = 1

        for key ,value in key_str_value_count.items():
            if value == 1:
                return s.index(key)
        return -1


print(Solution().firstUniqChar("leetcode"))