# -*- coding:utf-8 -*-
#@Time : 2021-05-27 19:57
#@Author: zxf_要努力
#@File : 贪心算法_55_跳跃游戏.py

'''
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

思路了解：
 就是每一步跳最远  每一步都计算一下从当前位置最远能够跳到哪里，
'''
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if 0 not in nums: return True  # 如果没有0则一定可以到达
        if len(nums) < 2: return True
        max_distance = nums[0]  # 设定可以达到的最大坐标
        for i in range(1, len(nums) - 1):
            if i <= max_distance:  # 表示当前坐标可以达到
                max_distance = max(max_distance, i + nums[i])  # 更新可以达到的最远坐标
            else:
                break
        return max_distance >= len(nums) - 1

    def canJump1(self,nums: List[int]) -> bool:
        if 0 not in nums:return True
        if len(nums) == 1: return True
        max_distance = nums[0]
        for i in range(1,len(nums)-1):
            if i <= max_distance:
                max_distance = max(max_distance,nums[i]+i)
            else:
                break
        return max_distance >= len(nums)-1


nums = [3,2,1,0,4]
print(Solution().canJump(nums))