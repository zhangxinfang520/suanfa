# -*- coding:utf-8 -*-
#@Time : 2021-06-09 22:59
#@Author: zxf_要努力
#@File : 28_实现strStr().py
'''
给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1
输入：haystack = "hello", needle = "ll"
输出：2
示例 2：

输入：haystack = "aaaaa", needle = "bba"
输出：-1
示例 3：

输入：haystack = "", needle = ""
输出：0

'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if haystack == "" and needle == "":
            return 0
        if haystack == "" :
            return -1
        if needle=="":
            return 0
        list_str1 = list(haystack)
        list_str2 = list(needle)
        if len(list_str2) > len(list_str1):
            return -1
        for i in  range(0,len(list_str1)):
            if list_str1[i] == list_str2[0]:
                j = i
                x = 0
                flag = True
                while x < len(list_str2) and flag:
                    if list_str2[x] != list_str1[j]:
                            flag = False
                    else:
                        x += 1
                        j += 1
                        if j==len(list_str1) and x==len(list_str2):
                            return i
                        if j >=len(list_str1) :
                            return -1

                if flag:
                    return i
        return -1
haystack = "a"

needle = "a"

print(Solution().strStr(haystack, needle))




