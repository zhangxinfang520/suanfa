# -*- coding:utf-8 -*-
#@Time : 2021-08-08 16:41
#@Author: zxf_要努力
#@File : offer_45_那数组排列成最小.py
'''
输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，
打印能拼接出的所有数字中最小的一个。

输入: [10,2]
输出: "102"

输入: [3,30,34,5,9]
输出: "3033459"

思路 ：
    题求拼接起来的最小数字，本质上是一个排序问题。设数组 numsnums 中任意两数字的字符串为 xx 和 yy ，则规定 排序判断规则 为：

    若拼接字符串 x + y > y + x，则 x “大于” y ；
        例如 "3" + "30"  > "30" + "3" 证明 "3" > "30" 这一题意味着 要把 "30" 放在"3"前面
     反之，若 x + y < y + x ，则 x “小于” y ；
'''
from typing import List


class Solution:

    def minNumber(self, nums: List[int]) -> str:
        strs = [str(num) for num in nums]
        def quick_sort(l,r):
            if l >=r : return
            i,j = l,r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j: j -=1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j: i +=1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(l,i-1)
            quick_sort(i+1,r)
        quick_sort(0,len(strs)-1)
        return "".join(strs)


print(Solution().minNumber([3, 30, 34, 5, 9]))

