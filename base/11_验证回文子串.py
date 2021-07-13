# -*- coding:utf-8 -*-
#@Time : 2021-07-13 12:21
#@Author: zxf_要努力
#@File : 11_验证回文子串.py
'''
输入: "A man, a plan, a canal: Panama"
输出: true
输入: "race a car"
输出: false
'''
ele = 'abcdefghijklmnopqrstuvwxyz0123456789'
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        end = len(s) - 1
        begin = 0

        while begin < end:
            while  s[begin].lower() not in ele:
                begin += 1
                if begin > end:
                    return True
            while s[end].lower() not in ele:
                end -= 1
                if begin > end:
                    return True
            if s[end].lower()!= s[begin].lower():
                return False
            else:
                begin += 1
                end -= 1
        return True

s = "a man, a plan, a canal: Panama"
s =".,"
print(Solution().isPalindrome(s))






