# -*- coding:utf-8 -*-
#@Time : 2021-07-03 22:20
#@Author: zxf_要努力
#@File : 217_存在重复元素.py
'''
给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。
如果数组中每个元素都不相同，则返回 false 。
'''
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_list = list(set(nums))
        return len(nums) == len(set_list)