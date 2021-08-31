# -*- coding:utf-8 -*-
#@Time : 2021/8/30 19:18
#@Author: zxf_要努力
#@File : 竞技世界.py

class Solution:
    def minSubArrayLen(self , s , nums ):
        # write code here
        res = []
        n = len(nums)
        nums.sort(reverse=True)
        def dp(track,target,idx):
            if target == 0:
                #res.append(len(track))
                if len(track) not in res:
                    res.append(len(track))
                return
            if idx == n:
                return
            for i in range(idx,n):
                if target - nums[i] >= 0:
                    track.append(nums[i])
                    dp(track,target-nums[i],i+1)
                    track.pop()
        dp([],s,0)
        return min(res)

if __name__ == '__main__':
    target,nums = 7, [2,3,1,2,4,3,7,2,5]
    print(Solution().minSubArrayLen(target, nums))
