# -*- coding:utf-8 -*-
#@Time : 2021-05-22 19:52
#@Author: zxf_要努力
#@File : 背包问题.py
'''
背包问题
吧=把物品的数量和 和装入的重量 限制的情况下  物品的价值最大
要明确状态和选择

状态就是
书包的还剩容量
还剩的物品

选择：
添不添加物品

base case

dp[0][:] =dp[:][0] = 0
因为没有物品或者背包没有空间的时候，能装的最大价值就是 0。
'''

def bagg(W,N,wt,val):
    '''

    :param W: 背包最多放物品重量
    :param N: 物品数量(一个背包最多放的物品的数量)
    :param wt: 每个物品的重量
    :param val: 每个物品的重量
    :return:
    '''
    #dp 数组代表物品的价值
    '''dp 数值的第一维代表 包里物品的数量
                第二维代表 背包的容量（重量）
    '''
    dp = [[0]*(W+1) for _ in range(N+1) ]
    for i in range(1,N+1):
        for w in range(1,W+1):
            #判断 是否还能不能放
            '''放物品i dp[i][w] = dp[i][w-wt[i-1]] + val[i]'''
            '''不放入物品i dp[i][w] = dp[i-1][w]'''
            if w - wt[i-1] < 0:
                #当前背包容量装不下，只能选择不装入背包
                dp[i][w] = dp[i - 1][w]
            #在背包放不放物品 i 的状态下 选取最大的状态
            else:
                dp[i][w] = max(dp[i-1][w-wt[i-1]]+val[i-1],dp[i-1][w])

    return dp[N][W]

N = 3
W = 4
wt = [2, 1, 3]
val = [4, 2, 3]
print(bagg(W,N,wt,val))