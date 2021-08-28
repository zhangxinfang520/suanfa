# -*- coding:utf-8 -*-
#@Time : 2021/8/25 19:20
#@Author: zxf_要努力
#@File : b站.py

#股票交易

import sys
import copy
#score 求解
if __name__ == '__main__':
    status = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    m = int(sys.stdin.readline().rstrip())
    n = len(status)
    dp = []
    for i in range(1,m+1):
        news_state = copy.copy(status)
        if status in dp and (dp.index(status)+1) != len(dp):
            status = dp[dp.index(status)+1]
        else:
            for j in range(len(status)-1):
                if (status[j-1] == 0 and status[j+1] == 0) or (status[j-1] == 1 and status[j+1]== 1):
                    news_state[j] = 0
                else:
                    news_state[j] = 1
            if (status[0] == 0 and status[n-2] == 0) or (status[0] == 1 and status[n-2]== 1):
                news_state[n-1] = 0
            else:
                news_state[n-1] = 1
            dp.append(news_state)
            status = news_state
    for x in status:
        print(x,end=" ")

