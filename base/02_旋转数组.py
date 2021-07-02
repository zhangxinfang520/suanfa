# -*- coding:utf-8 -*-
#@Time : 2021-07-02 21:46
#@Author: zxf_要努力
#@File : 02_旋转数组.py
'''
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
'''
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == k or k == 0:
            return
        if k > n:
            k = k % n
        before = nums[-k:]
        begin_index = n - k -1
        j = n - 1
        while begin_index >= 0:
            nums[j] = nums[begin_index]
            j -= 1
            begin_index -= 1
        x = 0
        for i in range(0,len(before)):
            nums[x] = before[i]
            x += 1
        return nums

    def other_method(self,nums: List[int], k: int):
        n = len(nums)
        if n == k or k == 0:
            return
        if k > n:
            k = k % n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)

        return nums

    def reverse(self,nums,start,end):
        while ( start < end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1




nums = [1,2,3,4,5,6,7]
k = 3
print(Solution().other_method(nums,k))