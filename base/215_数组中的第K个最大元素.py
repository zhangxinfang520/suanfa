# -*- coding:utf-8 -*-
#@Time : 2021-08-03 12:09
#@Author: zxf_要努力
#@File : 215_数组中的第K个最大元素.py
'''
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
'''
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #先写一个快排
        n = len(nums)

        def quick(num,l,r):
            if l < r:
                i, j = l ,r
                temp = num[i]
                while i < j:
                    while i< j and num[j] > temp:
                        j -= 1
                    if i < j:
                        num[i] = num[j]
                        i +=1
                    while i < j and num[i] < temp:
                        i +=1
                    if i < j:
                        num[j] = nums[i]
                        j -=1
                num[i] = temp
                quick(num,l,i-1)
                quick(num,i+1,r)
        quick(nums, 0, n-1)

        return nums[n-k]

nums = [3,2,1,5,6,4]
k = 2
print(Solution().findKthLargest(nums, k))