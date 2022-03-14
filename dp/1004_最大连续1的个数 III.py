# -*- coding:utf-8 -*-
#@Time : 2022/3/14 9:42
#@Author: zxf_要努力
#@File : 1004_最大连续1的个数 III.py

'''
给定一个二进制数组 nums 和一个整数 k ，如果可以翻转最多k 个 0 ，则返回 数组中连续 1 的最大个数 。
输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
数字从 0 翻转到 1，最长的子数组长度为 6。

输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
数字从 0 翻转到 1，最长的子数组长度为 10。

'''
class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) <= k:
            return len(nums)

        occ = list()
        n = len(nums)
        ans,rk = 0,-1
        for i in range(n):
            if i != 0:
                if nums[i-1] == 0:
                    k +=1
                occ.pop(0)
            while (rk + 1) < n and k > 0 :
                if nums[rk+1] == 0:
                    k -= 1
                occ.append(nums[rk + 1])
                rk +=1
            temp = rk+1
            while temp < n and nums[temp] == 1 :
                    temp +=1
            ans = max(ans,temp-i )
        return ans



if __name__ == '__main__':
    nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,1,0,1,1,1,1]
    K = 3
    solution = Solution()
    print(solution.longestOnes(nums, K))