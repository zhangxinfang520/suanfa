# -*- coding:utf-8 -*-
#@Time : 2021-06-08 22:36
#@Author: zxf_要努力
#@File : 384_打乱数组.py
'''
给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。
实现 Solution class:
Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果
输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

解释
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]

'''
from typing import List

import random

class Solution:

    def __init__(self, nums: List[int]):
        self.org_nums = nums
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.org_nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        nums = self.nums.copy()
        random.shuffle(nums)
        self.nums = nums
        return self.nums







nums = [1,2,3]
obj = Solution(nums)
param_1 = obj.reset()

param_2 = obj.shuffle()
param_3 = obj.shuffle()
print(param_1)
print(param_2)
print(param_3)