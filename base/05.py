# -*- coding:utf-8 -*-
#@Time : 2021-07-05 19:06
#@Author: zxf_要努力
#@File : 05.py
'''
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
输入：digits = [0]
输出：[1]
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = 1
        total_num = 0
        for num in digits[::-1]:
            total_num += num * i
            i *= 10
        total_num += 1
        return [int(i)for i in list(str(total_num))]

digits = [1,2,3]
print(Solution().plusOne(digits))

