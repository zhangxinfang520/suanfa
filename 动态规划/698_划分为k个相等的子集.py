# -*- coding:utf-8 -*-
#@Time : 2021-06-20 23:02
#@Author: zxf_要努力
#@File : 698_划分为k个相等的子集.py
'''
给定一个整数数组  nums 和一个正整数 k，
找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。

'''
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if k> len(nums):
            return False
        nums.sort(reverse=True)
        sum = 0
        for num in nums:
            sum += num
        if (sum % k) != 0:
            return False
        #理论上每一个桶里的和都为 sum/k
        target = int(sum / k)
        bucket = [0] * k
        a =  self.backtrack(nums,0,bucket,target)
        return a

    def backtrack(self,nums,index,bucket,target):
        if (index ==  len(nums)):
            for i in range(len(bucket)):
                if bucket[i] != target:
                    return False
            return True
        for i in range(len(bucket)):
            #预剪枝
            if bucket[i] + nums[index] > target:
                continue
            bucket[i] += nums[index]
            # 递归穷举下一个数字的选择
            if self.backtrack(nums,index+1,bucket,target):
                return True
            #撤销选择
            bucket[i] -= nums[index]

            # nums[index]装入哪个桶都不行
        return False

nums = [4, 3, 2, 3, 5, 2, 1]
print(Solution().canPartitionKSubsets(nums, 4))
# n= len(nums)
# def reverse(index):
#     if index == n:
#         return
#     else:
#         print(nums[index])
#         reverse(index+1)
# reverse(0)