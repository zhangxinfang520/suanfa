# -*- coding:utf-8 -*-
#@Time : 2021/8/29 17:22
#@Author: zxf_要努力
#@File : 360.py
import sys

def is_pass(b,p,q,a):
    if (p*a+q*b)/100 < 60:
        return False
    else:
        return True

def total_num(n,p,q,nums):
    #最多人数几个
    sum = 0
    nums.sort(reverse=True)
    dp = [100] * len(nums)
    flag = nums[0]
    for i in range(len(nums)):
        if nums[i] == flag:
            if is_pass(nums[i],p,q,dp[i]):
                sum +=1
            else:
                return sum
        else:
            dp[i] = dp[i-1] - 1
            flag = nums[i]
            if is_pass(nums[i],p,q,dp[i]):
                sum +=1
            else:
                return sum
    return sum




if __name__ == '__main__':
    #平时成绩占比为p 期末考试占比为q，平时分为a，期末考试分数为b 则总成绩为(p*a+q*b)/100
    # n 为学生数
    # n, p, q = list(map(int,sys.stdin.readline().strip().split()))
    # #期末分数
    # nums_list = list(map(int,sys.stdin.readline().strip().split()))
    n, p, q = 2,20,80
    nums_list = [51,50]
    res = total_num(n, p, q,nums_list)
    print(res)