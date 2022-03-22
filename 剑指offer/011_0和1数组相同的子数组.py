# encoding: utf-8
"""
@author: zxf_要努力
@file: 011_0和1数组相同的子数组.py
@time: 2022/3/14 18:09
"""

'''
给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度
输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量 0 和 1 的最长连续子数组。

'''

class Solution(object):
    def findMaxLength1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if sum(nums) == n // 2:
            return n
        #滑动窗口做

        res = 0
        for i in range(0,n):
            res = max(res,self.get_len(i,nums))
        return res

    def get_len(self,i,nums):
        n = len(nums)
        if i == n-1:
            return 0
        res = 0
        while i < n:
            if (n-i) % 2 == 0 and sum(nums[i:n]) == (n-i)//2:
                res = max(res,n-i)
            n -=1
        return res

    def findMaxLength(self, nums):
        # 0 转化为 -1 转化为 前缀和
        # 只要 两个 sum相同 证明 这两个sum之间 0和1之间 数量相等
        n = len(nums)
        if n == 0 : return 0

        res = 0
        sum_, memo = 0,dict()
        memo[0] = -1
        for i in range(n):
            sum_ += 1 if nums[i] == 1 else -1
            if sum_ in memo.keys():
                res = max(res,i-memo[sum_])
            else:
                memo[sum_] = i
        return res


if __name__ == '__main__':
    nums = [0,1,1,1,0,0]
    print(Solution().findMaxLength(nums))



