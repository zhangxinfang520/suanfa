# -*- coding:utf-8 -*-
#@Time : 2021-07-12 14:20
#@Author: zxf_要努力
#@File : 10.py
'''
集合 s 包含从 1 到 n 的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，
导致集合 丢失了一个数字 并且 有一个数字重复

'''

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        #需要返回重复值和缺失值
        #索引和数值相对应
        #通过将每个索引对应的元素变成负数，以表示这个索引被对应过一次了：
        n =len(nums)
        dup = -1
        for  i in range(n):
            index = abs(nums[i]) -1
            if nums[index] < 0:
                dup = abs(nums[i])
            else:
                nums[index]  *= -1

        missing = -1
        for i in range(n):
            if nums[i] > 0:
                missing = i+1
        return [dup,missing]


print(Solution().findErrorNums([1, 2, 3, 5, 7, 2, 4]))