# -*- coding:utf-8 -*-
#@Time : 2021/9/24 19:37
#@Author: zxf_要努力
#@File : 金山云.py

import sys

def get_mat_length(N,nums):
    res = 0
    temp = list(set(nums))
    nums = sorted(temp,key=nums.index)
    N = len(nums)
    for i in range(0,N-2):
        if i != 0 and nums[i-1] == nums[i]:
            continue
        for j in range(i+1,N-1):
            if j !=i+1 and nums[j-1] == nums[j]:
                continue
            k = N-1
            while j < k:
                if nums[i] < nums[j] and nums[j] < nums[k]:
                    res = max(res,nums[i]+nums[j]+nums[k])
                k -=1
    return res

def get_mat_length1(N,nums):
    N  = len(nums)
    res = 0
    if N < 3: return False
    small = float("-inf")
    middle = float("-inf")
    for i in range(N):
        if nums[i] >= small:
            small = nums[i]
        elif nums[i] >= middle:
            middle = nums[i]
        elif small < middle < nums[i]:
           res = max(res, small+middle+nums[i])
    return res



if __name__ == '__main__':
    # N = int(sys.stdin.readline().rstrip())
    # nums = list(map(int,sys.stdin.readline().rstrip().split()))
    N,nums = 6,[2,3,5,3,6,4]
    res = get_mat_length1(N,nums)
    print(res)