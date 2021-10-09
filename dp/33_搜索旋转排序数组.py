# -*- coding:utf-8 -*-
#@Time : 2021/10/9 9:39
#@Author: zxf_要努力
#@File : 33_搜索旋转排序数组.py
'''
整数数组 nums 按升序排列，数组中的值 互不相同 。
在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。
例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4
输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
输入：nums = [1], target = 0
输出：-1
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return -1 if target not in nums else nums.index(target)

    def search1(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    l = mid + 1
                else:
                    r = mid  - 1
        return -1

if __name__ == '__main__':
    nums = [7,8,9,1,2,3,4,5,6]
    print(Solution().search1(nums,5))
