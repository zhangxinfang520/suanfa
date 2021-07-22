# -*- coding:utf-8 -*-
#@Time : 2021-07-22 20:15
#@Author: zxf_要努力
#@File : 42_接雨水.py
'''
对于数组 height 中的每个元素，
分别向左和向右扫描并记录左边和右边的最大高度，然后计算每个下标位置能接的雨水量。
假设数组height 的长度为 nn
该做法需要对每个下标位置使用 O(n) 的时间向两边扫描并得到最大高度，
因此总时间复杂度是 O(n^2)。

'''
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],height[i])
        rightMax = [0] * (n - 1) + [height[n-1]]
        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])
        ans = sum(min(leftMax[i],rightMax[i]) - height[i] for i in range(n))
        return ans
    def other_method(self,height):
        n = len(height)
        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],height[i])
        rightMax = [0] * (n - 1) + [height[n-1]]
        for i in range(n-2,-1,-1):
            rightMax[i] = max(rightMax[i+1],height[i])

        ans = sum(min(leftMax[i],rightMax[i]) - height[i] for i in range(n))
        return ans

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().other_method(height))

