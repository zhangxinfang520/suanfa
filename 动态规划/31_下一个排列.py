# -*- coding:utf-8 -*-
#@Time : 2021-06-18 23:28
#@Author: zxf_要努力
#@File : 31_下一个排列.py
'''
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须 原地 修改，只允许使用额外常数空间。
输入：nums = [1,2,3]
输出：[1,3,2]
输入：nums = [3,2,1]
输出：[1,2,3]
输入：nums = [1,1,5]
输出：[1,5,1]
输入：nums = [1]
输出：[1]
'''
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = nums.copy()
        temp.sort()
        res = self.getall_sort(temp)
        i = res.index(nums)
        if i == len(res)-1:
            nums = res[0]
        else:
            nums = res[i+1]



    def getall_sort(self,nums:List[int]):
        n = len(nums)
        res = list()
        def traver(first=0):
            if first == n:
                res.append(nums[:])
            else:
                for i in range(first,n):
                    nums[first], nums[i] = nums[i], nums[first]
                    # 继续填充下一个数
                    traver(first + 1)
                    # 撤销操作
                    nums[first], nums[i] = nums[i], nums[first]
        traver()
        return res

nums = [1, 2, 3]
print(Solution().nextPermutation(nums))
