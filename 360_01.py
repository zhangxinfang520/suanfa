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


def get_count(n,k,m,w):
    if n == 0:
        return 0
    if n == 1:
        return max(w)
    w.sort()
    w_min_count = 0
    for i in range(len(w)):
        if w[i] <= m:
            w_min_count +=1
    if w_min_count == 0:
        count = n // k
        return sum(w[-count:])
    elif w_min_count == len(w):
        return sum(w)
    else:
        total = 0
        min_m = w[0:w_min_count]
        max_m = w[w_min_count:n]
        while  n > 0 and w_min_count > 0:
            if len(min_m) >= k and len(max_m) > 0:
                if sum(min_m[0:k])< max_m[-1]:
                    total += max_m.pop()
                    n = n-k
                    for i in range(0,k):
                        min_m.pop(0)
                else:
                    while n > 0 and len(min_m) > 0:
                        total += min_m.pop(0)
                    if n > 0:
                        total += max_m[-(n//k):]
                        return total
                    else:
                        return total
            else:
                if len(min_m) < k:
                    k = len(min_m)
                    total += sum(min_m)
                    n -= k
                    if n <= k:
                        total += max_m[-1]
                    else:
                        total += sum(max_m[-(n // k):])
                    return total
                else:
                    total += sum(min_m)
                    return total

if __name__ == '__main__':
    n, k, m = list(map(int,sys.stdin.readline().rstrip().split()))
    w = list(map(int, sys.stdin.readline().rstrip().split()))
    print(get_count(n, k, m, w))