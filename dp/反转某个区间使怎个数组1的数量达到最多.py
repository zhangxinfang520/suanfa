# -*- coding:utf-8 -*-
#@Time : 2022/3/14 11:20
#@Author: zxf_要努力
#@File : 反转某个区间使怎个数组1的数量达到最多.py

'''
反转某个区间使怎个数组1的数量达到最多
example
[1,0,0,1,0] -> [1,1,1,0,1]或者[1,1,1,1,0]
'''
class Solution:
    def reverse(self,nums):
        if len(nums) == 0:
            return -1
        n = len(nums)
        if n == sum(nums):
            return n-1
        ori = sum(nums)
        pre = ori
        ans = 0
        for r in nums:
            #判断当前这个0翻不翻 动态规划
            if r == 0:
                cur = max(pre+1,ori+1)
                ans = max(cur,ans)
                pre = ans
            else:
                cur = pre - 1
                pre = cur
        return ans

    def reverse2(self,nums):
        if len(nums) == 0:
            return -1
        ori = sum(nums)
        pre = ori
        ans = 0
        for r in nums:
            if r == 0:
                cur = max(pre+1,ori+1)
                ans = max(ans,cur)
                pre = cur
            else:
                cur = pre - 1
                pre = cur
        return ans

    def reverse1(self,nums):
        if len(nums) == 0:
            return -1
        max_nums, n = sum(nums), len(nums)
        if max_nums == n:
            return n - 1
        #将所有的 0 设定为-1
        dp = [1] * n
        for i in range(n):
            if nums[i] == 1:
                dp[i] = -1
        #开始和结束下表
        left,right = 0,0
        sum_, ans = dp[0],dp[0]
        for i in range(1,n):
            # 如果当前的和比之前的小更新子数组的开始下标
            if dp[i] > dp[i] + sum_:
                left = i
            sum_ = max(dp[i], dp[i] + sum_)
            # 如果当前的和比前的大那更新子数组的结束下标
            if ans < sum_:
                right = i
            ans = max(ans,sum_)
        return left,right

    def reverse3(self,nums):
        if len(nums) == 0:
            return -1
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            if nums[i] == 1:
                dp[i] = -1
        left,right = 0,0
        ans,res = dp[0],dp[0]
        for i in range(1,n):
            if dp[i] > dp[i] + ans:
                left = i
            ans = max(dp[i],dp[i] + ans)
            if res < ans:
                right = i
            res = max(res,ans)
        return left,right

if __name__ == '__main__':
    nums = [0,1,1,1,1,1,1,1,1]
    solution  = Solution()
    print(solution.reverse3(nums))


