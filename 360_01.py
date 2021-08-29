# -*- coding:utf-8 -*-
#@Time : 2021/8/29 17:22
#@Author: zxf_要努力
#@File : 360.py
'''

长城上有连成一排的n个烽火台，每个烽火台都有士兵驻守。
第i个烽火台驻守着ai个士兵，相邻峰火台的距离为1。
另外，有m位将军，每位将军可以驻守一个峰火台，
每个烽火台可以有多个将军驻守，将军可以影响所有距离他驻守的峰火台小于等于x的烽火台。
每个烽火台的基础战斗力为士兵数，另外，每个能影响此烽火台的将军都能使这个烽火台的战斗力提升k。
长城的战斗力为所有烽火台的战斗力的最小值。
请问长城的最大战斗力可以是多少？
第一行四个正整数n,m,x,k(1<=x<=n<=10^5,0<=m<=10^5,1<=k<=10^5)
第二行n个整数ai(0<=ai<=10^5)
'''
import sys



if __name__ == '__main__':

    x = list(map(int, input().split()))
    n, m, x, k = x[0], x[1], x[2], x[3]
    nums = list(map(int, input().split()))
    score_min = min(nums)
    if m == 0:
        print(score_min)

    def fun(nums, target, m, x, k):
        diff = [0] * len(nums)
        diff[0] = nums[0]
        for i in range(1, len(nums)):
            diff[i] = nums[i] - nums[i - 1]
        cur = 0
        for i in range(0, len(nums)):
            cur += diff[i]
            if cur < target:
                use = (target - cur + k - 1) // k
                m -= use
                if m < 0:
                    return False
                cur += use * k
                if i + 2 * x + 1 < len(nums):
                    diff[i + 2 * x + 1] -= use * k
        return m >= 0


    left = score_min
    right = score_min + m * k
    while left < right:
        mid = left + (right - left + 1) // 2
        if fun(nums, mid, m, x, k):
            left = mid
        else:
            right = mid - 1

    print(int(left))