# -*- coding:utf-8 -*-
#@Time : 2021-05-28 22:12
#@Author: zxf_要努力
#@File : 贪心问题_45_跳跃问题2.py
'''
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
假设你总是可以到达数组的最后一个位置。

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
  从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
输入: [2,3,0,1,4]
输出: 2
'''
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return True
        max_distance = 0
        end,jumps = 0,0
        for i in range(0,len(nums)-1):
            # 每次跳一个点 在该点的值的范围内找下一次调到最大值
            max_distance = max(nums[i]+i,max_distance)
            if end == i:
                jumps +=1
                end = max_distance
        return jumps