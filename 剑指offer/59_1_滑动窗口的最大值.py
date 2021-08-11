# -*- coding:utf-8 -*-
# @Time : 2021-08-10 17:01
# @Author: zxf_要努力
# @File : 59_1_滑动窗口的最大值.py
'''
给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

'''
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return [max(nums)]
        if k == 1:
            return nums
        re, n = [], len(nums)
        for i in range(n):
            if i + k > n:
                break
            else:
                temp = nums[i:i + k]
                re.append(max(temp))
        return re
    
    def other(self, nums, k):
        res, heap = [], []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i],i))
            if i+1 >=k:
                #要判断第一个值是否在这个滑动窗口了
                while heap and heap[0][1] < i - k + 1 :
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res


class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # nums = [1, 3, -1, -3, 5, 3, 6, 7]
        # how to get max value among the window
        # use maximum heap (-value, index)

        # Time complexity : O(NlogN)
        # Space complexity: O(N)

        res, heap = [], []
        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            if i + 1 >= k:
                while heap and heap[0][1] < i + 1 - k:
                    heapq.heappop(heap)
                res.append(-heap[0][0])
        return res


nums = [1,3,-1,-3,5,3,6,7]
k = 3
# nums = [9, 11]
# k = 1
print(Solution().maxSlidingWindow(nums, k))
print(Solution().other(nums, k))
