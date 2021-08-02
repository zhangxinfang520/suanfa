# -*- coding:utf-8 -*-
#@Time : 2021-08-02 10:53
#@Author: zxf_要努力
#@File : 560_和为K的子数组.py
#给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

'''我的思路 滑动窗口试一下 自己感觉不太行'''

'''
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
'''
class  Solution:
    def subarraySum(self,nums,K):
        n = len(nums)
        if n == 0:return 0
        if n == 1 and nums[-1] == K : return 1
        ans = 0
        for i in range(1,n+1):
            for j in range(0,i):
                if sum(nums[j:i]) == K:
                    ans +=1
        return ans

    def subarraySum1(self,nums,K):
        #这里时间复杂度为 n**2 基本和第一种方法一样
        #通过构造前缀 来减少遍历
        n = len(nums)
        if n == 0: return 0
        if n == 1 and nums[-1] == K: return 1
        #前缀数组 sum[i] 代表 nums[0:i]的和
        sum = [0] * (n+1)

        for i in range(n):
            sum[i+1] = sum[i] + nums[i]

        ans = 0
        for i in range(1,n+1):
            for j in range(0,i):
                if (sum[i] - sum[j]) == K:
                    ans +=1
        return ans

    def subarraySum2(self, nums, K):
        # 通过构造前缀 来减少遍历 同时借助于hashmap python 为字典
        n = len(nums)
        if n == 0: return 0
        if n == 1 and nums[-1] == K: return 1
        re_dict = dict()
        re_dict[0] = 1
        ans, sum_ = 0, 0
        for i in range(n):
            sum_ += nums[i]
            # 这是我们想找的前缀和nums[0..j]
            sum_j = sum_ - K
            # 如果前面有这个前缀和，则直接更新答案
            if sum_j in re_dict.keys():
                ans += re_dict[sum_j]
            #把前缀和 nums[0..i] 加入并记录出现次数
            re_dict[sum_] = re_dict.get(sum_, 0) + 1
        return ans

print(Solution().subarraySum2([1,1,2,1,2], 3))