# -*- coding:utf-8 -*-
#@Time : 2021-07-14 14:37
#@Author: zxf_要努力
#@File : 27_移除元素.py
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，
# 并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        fast,slow = 0,0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow


nums = [4,5]
val = 5

print(Solution().removeElement(nums, val))

