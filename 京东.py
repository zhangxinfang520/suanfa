# -*- coding:utf-8 -*-
#@Time : 2021/8/21 19:29
#@Author: zxf_要努力
#@File : 京东.py
import sys
if __name__ == '__main__':
    #n, a, b, c = list(map(int,sys.stdin.readline().strip().split(" ")))
    n, a, b, c = 6, 2, 3, 4
    #思路 题没有读懂 后面的abc 干嘛的 分为三段？
    res = []
    temp = [a,b,c]
    len_n = len(temp)

    def dp(track,target,idx):
        if target == 0:
            res.append(len(track))
            return
        if idx == len_n:
            return
        dp(track,target,idx+1)
        if target - temp[idx] >= 0:
            track.append(temp[idx])
            target -= temp[idx]
            dp(track, target, idx)
            target += temp[idx]
            track.pop()
    dp([],n,0)
    print(max(res))




